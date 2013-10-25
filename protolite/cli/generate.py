import json
import os
import re
import argparse
import logging
import itertools

from collections import defaultdict

from antlr3 import ANTLRFileStream, CommonTokenStream

from protolite.parse import proto_parser
from protolite.parse import proto_lexer

log = logging.getLogger(__name__)


ignore_types = [
    proto_parser.OPTION_LITERAL,
    proto_parser.IMPORT_LITERAL,
]


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
  return path


def underscore(camel, prefix=None):
    if prefix is not None:
        if camel.startswith(prefix):
            camel = camel[len(prefix):]
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


def output_info(proto, output):
    path = os.path.basename(proto)
    module, _ = os.path.splitext(path)
    path = module + '.py'
    return module, os.path.join(output, path)


def _parse(tree, prefix=None):
    if tree is None or tree.getType() in ignore_types:
        return None

    if tree.getType() == proto_parser.PACKAGE_LITERAL:
        # TODO should the package be used as a namespace?
        return None

    children =[]
    for child in tree.getChildren():
        _child = _parse(child, prefix)
        if _child:
            children.append(_child)

    # top-level
    if tree.getType() == proto_parser.PROTO:
        return dict(children)

    if tree.getType() in [proto_parser.MESSAGE_LITERAL, proto_parser.ENUM_LITERAL]:
        name = children.pop(0)
        name = underscore(name.getText(), prefix=prefix)
        return name, dict(children)

    if tree.getType() == proto_parser.MESSAGE_FIELD:
        scope, field_type, field_name, field_number = children
        fields = dict()
        fields['type'] = underscore(field_type.getText(), prefix=prefix)
        if field_type.getType() == proto_parser.IDENTIFIER:
            # enum ,embedded or repeated
            fields['message'] = fields['type']
            fields['type'] = 'embedded'
            if scope.getText() == 'repeated':
                fields['type'] = 'repeated'
        fields['name'] = underscore(field_name.getText(), prefix=prefix)
        field_number = int(field_number.getText())
        return field_number, fields

    if tree.getType() == proto_parser.ENUM_FIELD:
        enum_name, enum_number = children
        enum_name = underscore(enum_name.getText(), prefix=prefix)
        enum_number = int(enum_number.getText())
        return enum_number, enum_name

    return tree


def parse(tree, prefix=None):
    proto = _parse(tree, prefix=prefix)
    decoding = dict()
    dec_messages = defaultdict(dict)
    enc_messages = defaultdict(dict)
    for name, fields in proto.items():
        for field, info in fields.items():
            if info.get('type') in ['embedded', 'repeated']:
                message = info.pop('message')
                if message in fields:
                    # enum
                    message = '{name}["{message}"]'.format(
                        name=name,
                        message=message,
                    )
                    info['type'] = 'enum'
                dec_messages[name][field] = message
                enc_messages[name][info['name']] = message
        decoding[name] = fields

    encoding = dict()
    enums = dict()
    for name, fields in decoding.items():
        _fields = dict()
        for field, info in fields.items():
            _type = info.get('type')
            if not _type:
                # enum definition
                _info = dict([(v,k) for k,v in info.items()])
                _fields[field] = _info
                enums[field] = _info
                continue
            _info = dict([
                ('type', _type),
                ('field', field),
            ])
            _fields[info['name']] = _info
        encoding[name] = _fields

    return decoding, dec_messages, encoding, enc_messages, enums


def _order(proto):
    _dir = os.path.dirname(proto)
    root = root_rule(proto)
    for child in root.getChildren():
        if child.getType() == proto_parser.IMPORT_LITERAL:
            depend, = child.getChildren()
            depend = depend.getText().strip('"')
            depend = os.path.join(_dir, depend)
            depend = abs_path(depend)
            for depend in _order(depend):
                yield depend
    yield proto


def order(protos):
    done = []
    for proto in protos:
        for depend in _order(proto):
            if any([os.path.samefile(d, depend) for d in done]):
                continue
            yield depend
            done.append(depend)
    if proto not in done:
        yield proto


def write_references(fp, coding, messages, fields, imports):
    fp.write('\n')
    for name, _fields in messages.items():
        for field, message in _fields.items():
            _message = message.rsplit('[')
            _message = _message[0]
            depend = ''
            if not _message in fields:
                for module, __fields in imports.items():
                    if _message in __fields:
                        depend = module + '.'
                        break
                if not depend:
                    raise ValueError(
                        'attribute is not in any module: {_message}'.format(
                            _message=_message,
                        )
                    )
            if coding == 'encoding':
                field = '"{field}"'.format(field=field)
            fp.write(
                '\n{coding}.{name}[{field}]["message"] = '
                '{depend}{coding}.{message}'.format(
                    coding=coding,
                    depend=depend,
                    name=name,
                    field=field,
                    message=message,
                ),
            )


def create(protos, output, prefix):
    proto_json = ProtoJSON(indent=8, separators=(',', ': '))
    imports = dict()
    for proto in order(protos):
        log.info('Processing {proto}'.format(proto=proto))
        root = root_rule(proto)
        decoding, dec_messages, encoding, enc_messages, enums = parse(root, prefix)
        module, path = output_info(proto, output)
        with open(path, 'w') as fp:
            for _import in imports.keys():
                fp.write('import {_import}\n'.format(_import=_import))
            for name, enums in enums.items():
                fp.write('class {name}(object):'.format(name=name))
                for enum, value in enums.items():
                    fp.write(
                        '\n    {enum} = {value}'.format(enum=enum, value=value),
                    )
                fp.write('\n\n')
            fp.write('\nclass decoding(object):')
            for name, value in decoding.items():
                value = ''.join(proto_json.iterencode(value))
                fp.write(
                    '\n    {name} = {value}'.format(name=name, value=value),
                )
            write_references(
                fp,
                'decoding',
                dec_messages,
                decoding.keys(),
                imports,
            )
            fp.write('\n\nclass encoding(object):')
            for name, value in encoding.items():
                value = ''.join(proto_json.iterencode(value))
                fp.write(
                    '\n    {name} = {value}'.format(name=name, value=value),
                )
            write_references(
                fp,
                'encoding',
                enc_messages,
                encoding.keys(),
                imports,
            )
            fp.write('\n')
        imports[module] = decoding.keys()


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
        '--prefix',
        help='prefix to remove from protobuf names',
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
    create(protos, output, args.prefix)
