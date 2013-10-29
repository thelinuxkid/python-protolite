import json
import os
import re
import logging

from collections import defaultdict, OrderedDict

from antlr3 import ANTLRFileStream, CommonTokenStream

from util import abs_path
from parse import proto_parser
from parse import proto_lexer

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
    def iterencode(self, obj, prefixes):
        data = json.JSONEncoder.iterencode(self, obj)
        for value in data:
            value = underscore(value, prefixes=prefixes)
            stripped = value.strip('"')
            if stripped.isdigit():
                value = stripped
            yield value


def underscore(camel, prefixes=[]):
    prefixes.sort(key=len, reverse=True)
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


def _parse(tree):
    def _literal(children):
        name = children.pop(0).getText()
        return name, OrderedDict(children)

    if tree is None or tree.getType() in ignore_types:
        return None

    children =[]
    for child in tree.getChildren():
        _child = _parse(child)
        if _child:
            children.append(_child)

    _type = tree.getType()
    # top-level
    if _type == proto_parser.PROTO:
        return OrderedDict(children)

    if _type == proto_parser.MESSAGE_LITERAL:
        return _literal(children)

    if _type == proto_parser.ENUM_LITERAL:
        name, children = _literal(children)
        children['type'] = 'enum_literal'
        return name, OrderedDict(children)

    if _type == proto_parser.MESSAGE_FIELD:
        scope, field_type, field_name, field_number = children
        fields = OrderedDict()
        field_number = int(field_number.getText())
        fields['name'] = field_name.getText()
        fields['type'] = field_type.getText()
        if field_type.getType() == proto_parser.IDENTIFIER:
            _tree = tree.getParent()
            while _tree:
                for child in _tree.children:
                    if (child.getType() == proto_parser.ENUM_LITERAL and
                        child.children[0].getText() == field_type.getText()
                    ):
                        fields['type'] = 'enum'
                        return field_number, fields
                _tree = _tree.getParent()
            fields['message'] = fields['type']
            fields['type'] = 'embedded'
            if scope.getText() == 'repeated':
                fields['type'] = 'repeated'
        return field_number, fields

    if _type == proto_parser.ENUM_FIELD:
        enum_name, enum_number = children
        enum_name = enum_name.getText().upper()
        enum_number = int(enum_number.getText())
        return enum_number, enum_name

    return tree


def parse(tree, prefixes=[]):
    proto = _parse(tree)
    decoding = OrderedDict()
    dec_refs = DefaultOrderedDict(OrderedDict)
    enc_refs = DefaultOrderedDict(OrderedDict)
    enums = OrderedDict()
    for name, fields in proto.items():
        _fields = DefaultOrderedDict(OrderedDict)
        for field, info in fields.items():
            if info['type'] == 'enum_literal':
                enum = OrderedDict(
                    [(v,k) for k,v in info.items() if k != 'type']
                )
                enums[field] = enum
                continue
            if info['type'] in ['embedded', 'repeated']:
                reference = info.pop('message')
                dec_refs[name][field] = reference
                enc_refs[name][info['name']] = reference
            _fields[field] = info
        decoding[name] = _fields

    encoding = OrderedDict()
    for name, fields in decoding.items():
        _fields = DefaultOrderedDict(OrderedDict)
        for field, info in fields.items():
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


def write_references(fp, references, fields, imports, prefixes):
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
                name = underscore(name, prefixes=prefixes)
                reference = underscore(reference, prefixes=prefixes)
                if coding == 'encoding':
                    field = underscore(field, prefixes=prefixes)
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


def generate(protos, output, prefixes):
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
                name = underscore(name, prefixes=prefixes)
                fp.write('class {name}(object):'.format(name=name))
                for enum, value in enums.items():
                    fp.write(
                        '\n    {enum} = {value}'.format(enum=enum, value=value),
                    )
                fp.write('\n\n')
            for name, _fields in attrs.items():
                fp.write('\nclass {name}(object):'.format(name=name))
                for field, value in _fields.items():
                    value = ''.join(proto_json.iterencode(value, prefixes))
                    field = underscore(field, prefixes=prefixes)
                    fp.write(
                        '\n    {field} = {value}'.format(field=field, value=value),
                    )
                fp.write('\n')
            write_references(
                fp,
                references,
                fields,
                depends,
                prefixes,
            )
            fp.write(
                '\n{convenience}\n'.format(convenience=convenience_coder),
            )
            for field in fields:
                field = underscore(field, prefixes=prefixes)
                fp.write(
                    '{field} = convenience_coder(decoding.{field}, '
                    'encoding.{field})\n'.format(
                        field=field,
                    )
                )
        done[module] = fields
