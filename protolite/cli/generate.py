import json
import os
import re
import argparse
import logging
import itertools

from collections import defaultdict, OrderedDict

from antlr3 import ANTLRFileStream, CommonTokenStream

from protolite.parse import proto_parser
from protolite.parse import proto_lexer

log = logging.getLogger(__name__)


ignore_types = [
    proto_parser.OPTION_LITERAL,
    proto_parser.IMPORT_LITERAL,
    proto_parser.PACKAGE_LITERAL,
]

convenience_coder = """
class convenience_coder(object):
    def __init__(self, decoding, encoding):
        self.decoding = decoding
        self.encoding = encoding

    def decode(self, message):
        return protolite.decode(self.decoding, message)

    def encode(self, message):
        return protolite.encode(self.encoding, message)
"""


class DefaultOrderedDict(defaultdict, OrderedDict):
    def __init__(self, default_factory):
        defaultdict.__init__(self, default_factory)
        OrderedDict.__init__(self)


class ProtoJSON(json.JSONEncoder):
    def iterencode(self, obj):
        data = json.JSONEncoder.iterencode(self, obj)
        for value in data:
            stripped = value.strip('"')
            if stripped.isdigit():
                value = stripped
            yield value


def abs_path(path):
  path = os.path.expanduser(path)
  path = os.path.abspath(path)
  path = os.path.realpath(path)
  path = os.path.normpath(path)
  return path


def underscore(camel, prefixes=[]):
    prefixes = sorted(prefixes, key=len, reverse=True)
    for prefix in prefixes:
        if camel.startswith(prefix):
            camel = camel[len(prefix):]
            break
    under = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel)
    under = re.sub('([a-z0-9])([A-Z])', r'\1_\2', under).lower()
    return under


def root_rule(proto):
    stream = ANTLRFileStream(proto)
    lexer = proto_lexer.proto_lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = proto_parser.proto_parser(tokens)
    rule = parser.proto()
    return rule.tree


def output_path(proto, output):
    path = os.path.basename(proto)
    path, _ = os.path.splitext(path)
    path = path + '.py'
    return os.path.join(output, path)


def _parse(tree, prefixes=[]):
    if tree is None or tree.getType() in ignore_types:
        return None

    children =[]
    for child in tree.getChildren():
        _child = _parse(child, prefixes)
        if _child:
            children.append(_child)

    # top-level
    if tree.getType() == proto_parser.PROTO:
        return OrderedDict(children)

    if tree.getType() in [proto_parser.MESSAGE_LITERAL, proto_parser.ENUM_LITERAL]:
        name = children.pop(0)
        name = underscore(name.getText(), prefixes=prefixes)
        return name, OrderedDict(children)

    if tree.getType() == proto_parser.MESSAGE_FIELD:
        scope, field_type, field_name, field_number = children
        fields = OrderedDict()
        fields['type'] = underscore(field_type.getText(), prefixes=prefixes)
        if field_type.getType() == proto_parser.IDENTIFIER:
            # enum ,embedded or repeated
            fields['message'] = fields['type']
            fields['type'] = 'embedded'
            if scope.getText() == 'repeated':
                fields['type'] = 'repeated'
        fields['name'] = underscore(field_name.getText(), prefixes=prefixes)
        field_number = int(field_number.getText())
        return field_number, fields

    if tree.getType() == proto_parser.ENUM_FIELD:
        enum_name, enum_number = children
        enum_name = underscore(enum_name.getText(), prefixes=prefixes)
        enum_number = int(enum_number.getText())
        return enum_number, enum_name

    return tree


def parse(tree, prefixes=[]):
    proto = _parse(tree, prefixes=prefixes)
    decoding = OrderedDict()
    dec_refs = DefaultOrderedDict(OrderedDict)
    enc_refs = DefaultOrderedDict(OrderedDict)
    enums = OrderedDict()
    for name, fields in proto.items():
        _fields = DefaultOrderedDict(OrderedDict)
        for field, info in fields.items():
            _type = info.get('type')
            if _type in ['embedded', 'repeated']:
                reference = info.pop('message')
                if reference in fields:
                    enum = fields[reference]
                    _fields['enums'][reference] = enum
                    reference = '{name}["enums"]["{reference}"]'.format(
                            name=name,
                            reference=reference,
                        )
                    info['type'] = 'enum'
                dec_refs[name][field] = reference
                enc_refs[name][info['name']] = reference
            if _type:
                _fields[field] = info
        decoding[name] = _fields

    encoding = OrderedDict()
    for name, fields in decoding.items():
        _fields = DefaultOrderedDict(OrderedDict)
        for field, info in fields.items():
            if field == 'enums':
                for _name, values in info.items():
                    values = OrderedDict([(v,k) for k,v in values.items()])
                    _fields['enums'][_name] = values
                    enums[_name] = values
                continue
            _info = OrderedDict([
                ('type', info['type']),
                ('field', field),
            ])
            _fields[info['name']] = _info
        encoding[name] = _fields

    attrs = OrderedDict([
        ('decoding', decoding),
        ('encoding', encoding)
    ])
    references = OrderedDict([
        ('decoding', dec_refs),
        ('encoding', enc_refs),
    ])
    return attrs, references, enums


def _order(proto):
    module = os.path.basename(proto)
    module, _ = os.path.splitext(module)
    _dir = os.path.dirname(proto)
    root = root_rule(proto)
    imports = []
    for child in root.getChildren():
        if child.getType() == proto_parser.IMPORT_LITERAL:
            path, = child.getChildren()
            path = path.getText().strip('"')
            _module, _ = os.path.splitext(path)
            imports.append(_module)
            path = os.path.join(_dir, path)
            path = abs_path(path)
            for path, _module, _imports in _order(path):
                yield path, _module, _imports
    yield proto, module, imports


def order(protos):
    done = []
    for proto in protos:
        for path, module, imports in _order(proto):
            if any([os.path.samefile(d, path) for d in done]):
                continue
            yield path, module, imports
            done.append(path)


def write_references(fp, references, fields, imports):
    for coding, _references in references.items():
        for name, _fields in _references.items():
            for field, reference in _fields.items():
                _reference = reference.rsplit('[')
                _reference = _reference[0]
                depend = ''
                if _reference not in fields:
                    for module, __fields in imports.items():
                        if _reference in __fields:
                            depend = module + '.'
                            break
                    if not depend:
                        raise ValueError(
                            'attribute is not in any module: {_message}'.format(
                                _reference=_reference,
                            )
                        )
                if coding == 'encoding':
                    field = '"{field}"'.format(field=field)
                fp.write(
                    '\n{coding}.{name}[{field}]["message"] = '
                    '{depend}{coding}.{reference}'.format(
                        coding=coding,
                        depend=depend,
                        name=name,
                        field=field,
                        reference=reference,
                    ),
                )
        fp.write('\n')


def create(protos, output, prefixes):
    proto_json = ProtoJSON(indent=8, separators=(',', ': '))
    done = dict()
    for path, module, imports in order(protos):
        log.info('Processing {path}'.format(path=path))
        root = root_rule(path)
        attrs, references, enums = parse(root, prefixes)
        fields = attrs['decoding'].keys()
        depends = dict([(k,v) for k,v in done.items() if k in imports])
        path = output_path(path, output)
        with open(path, 'w') as fp:
            fp.write('import protolite\n')
            for _import in imports:
                fp.write('import {_import}\n'.format(_import=_import))
            fp.write('\n')
            for name, enums in enums.items():
                fp.write('class {name}(object):'.format(name=name))
                for enum, value in enums.items():
                    fp.write(
                        '\n    {enum} = {value}'.format(enum=enum, value=value),
                    )
                fp.write('\n\n')
            for name, fields in attrs.items():
                fp.write('\nclass {name}(object):'.format(name=name))
                for field, value in fields.items():
                    value = ''.join(proto_json.iterencode(value))
                    fp.write(
                        '\n    {field} = {value}'.format(field=field, value=value),
                    )
                fp.write('\n')
            write_references(
                fp,
                references,
                fields,
                depends,
            )
            fp.write(
                '\n{convenience}\n'.format(convenience=convenience_coder),
            )
            for field in fields:
                fp.write(
                    '{field} = convenience_coder(decoding.{field}, '
                    'encoding.{field})\n'.format(
                        field=field,
                    )
                )
        done[module] = fields


def parse_args():
    parser = argparse.ArgumentParser(
        description='create alternate Python protobuf files',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
        help='output DEBUG logging statements (default: %(default)s)',
    )
    parser.add_argument(
        '--protos',
        help='path(s) to the protocol buffer definition file(s)',
        required=True,
        metavar='PATH',
        nargs='+',
        action='append',
        type=str,
    )
    parser.add_argument(
        '--output',
        help='path to the directory in which to store the results',
        required=True,
        metavar='PATH',
        type=str,
    )
    parser.add_argument(
        '--prefixes',
        help='prefixes to remove from protobuf names',
        nargs='+',
        action='append',
        type=str,
        default=None,
    )
    return parser.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format='%(asctime)s.%(msecs)03d %(name)s: %(levelname)s: %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S',
    )
    protos = itertools.chain(*args.protos)
    protos = [abs_path(proto) for proto in protos]
    output = abs_path(args.output)
    if not os.path.exists(output):
        os.mkdir(output)
    prefixes = list(itertools.chain(*args.prefixes))
    create(protos, output, prefixes)
