import json
import os
import re
import argparse
import logging
import itertools

from collections import OrderedDict, deque, defaultdict

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
        values = []
        for value in data:
            stripped = value.strip('"')
            if stripped.isdigit():
                value = stripped
            values.append(value)
        return values

def abs_path(path):
  path = os.path.expanduser(path)
  path = os.path.abspath(path)
  return path


def to_underscore(camel, prefix=None):
    if prefix is not None:
        if camel.startswith(prefix):
            camel = camel[len(prefix):]
    under = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel)
    under = re.sub('([a-z0-9])([A-Z])', r'\1_\2', under).lower()
    return under


def _proto_dict(tree, prefix=None):
    def _literal(children):
        name = children.pop(0)
        name = to_underscore(name.getText(), prefix=prefix)
        return name, dict(children)

    if tree is None or tree.getType() in ignore_types:
        return None

    if tree.getType() == proto_parser.PACKAGE_LITERAL:
        # TODO should the package be used as a namespace?
        return None

    children =[]
    for child in tree.getChildren():
        _child = _proto_dict(child, prefix)
        if _child:
            children.append(_child)

    # top-level
    if tree.getType() == proto_parser.PROTO:
        return dict(children)

    if tree.getType() == proto_parser.MESSAGE_LITERAL:
        return _literal(children)

    if tree.getType() == proto_parser.ENUM_LITERAL:
        name, children = _literal(children)
        children['type'] = 'enum_definition'
        return name, children

    if tree.getType() == proto_parser.MESSAGE_FIELD:
        scope, field_type, field_name, field_number = children
        fields = dict()
        fields['type'] = to_underscore(field_type.getText(), prefix=prefix)
        if field_type.getType() == proto_parser.IDENTIFIER:
            # enum ,embedded or repeated
            fields['message'] = fields['type']
            fields['type'] = 'embedded'
            if scope.getText() == 'repeated':
                fields['type'] = 'repeated'
        fields['name'] = to_underscore(field_name.getText(), prefix=prefix)
        field_number = int(field_number.getText())
        return field_number, fields

    if tree.getType() == proto_parser.ENUM_FIELD:
        enum_name, enum_number = children
        enum_name = to_underscore(enum_name.getText(), prefix=prefix)
        enum_number = int(enum_number.getText())
        return enum_number, enum_name

    return tree


def proto_dict(tree, prefix=None):
    proto = _proto_dict(tree, prefix=prefix)
    decoding = deque()
    dec_messages = defaultdict(dict)
    enc_messages = defaultdict(dict)
    # enum definitions at the top
    for name, fields in proto.items():
        for field, info in fields.items():
            # TODO this probably isn't safe
            if info['type'] == 'enum_definition':
                del fields[field]
                decoding.appendleft((field, info))
            if info['type'] in ['embedded', 'repeated']:
                message = info.pop('message')
                dec_messages[name][field] = message
                enc_messages[name][info['name']] = message
            decoding.append((name, fields))
    decoding = OrderedDict(decoding)

    encoding = OrderedDict()
    for name, fields in decoding.items():
        _fields = dict()
        _type = fields.pop('type', None)
        for field, info in fields.items():
            if _type == 'enum_definition':
                _fields[info] = field
                continue
            _info = dict([
                ('type', info['type']),
                ('field', field),
            ])
            _fields[info['name']] = _info
        encoding[name] = _fields

    return decoding, dec_messages, encoding, enc_messages


def root_rule(proto):
    stream = ANTLRFileStream(proto)
    lexer = proto_lexer.proto_lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = proto_parser.proto_parser(tokens)
    rule = parser.proto()
    return rule.tree


def proto_order(proto):
    _dir = os.path.dirname(proto)
    root = root_rule(proto)
    for child in root.getChildren():
        if child.getType() == proto_parser.IMPORT_LITERAL:
            depend, = child.getChildren()
            depend = depend.getText().strip('"')
            depend = os.path.join(_dir, depend)
            depend = abs_path(depend)
            for depend in proto_order(depend):
                yield depend
    yield proto


def protos_order(protos):
    done = []
    for proto in protos:
        for depend in proto_order(proto):
            if any([os.path.samefile(d, depend) for d in done]):
                continue
            yield depend
            done.append(depend)
    if proto not in done:
        yield proto


def create_proto(protos, output, prefix):
    for proto in protos_order(protos):
        log.info('Processing {proto}'.format(proto=proto))
        root = root_rule(proto)
        decoding, dec_messages, encoding, enc_messages = proto_dict(root, prefix)
        proto_json = ProtoJSON(indent=8, separators=(',', ': '))
        path = os.path.basename(proto)
        path, _ = os.path.splitext(path)
        path += '.py'
        path = os.path.join(output, path)
        with open(path, 'w') as fp:
            fp.write('class decoding(object):')
            for name, value in decoding.items():
                value = ''.join(proto_json.iterencode(value))
                fp.write(
                    '\n    {name} = {value}'.format(name=name, value=value),
                )
            for name, fields in dec_messages.items():
                for field, info in fields.items():
                    fp.write(
                        '\ndecoding.{name}[{field}]["message"] = '
                        'decoding.{info}'.format(
                            name=name,
                            field=field,
                            info=info.strip('"'))
                        ,
                    )
        with open(path, 'a') as fp:
            fp.write('\n\nclass encoding(object):')
            for name, value in encoding.items():
                value = ''.join(proto_json.iterencode(value))
                fp.write(
                    '\n    {name} = {value}'.format(name=name, value=value),
                )
            for name, fields in enc_messages.items():
                for field, info in fields.items():
                    fp.write(
                        '\nencoding.{name}["{field}"]["message"] = '
                        'encoding.{info}'.format(
                            name=name,
                            field=field,
                            info=info.strip('"'))
                        ,
                    )


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
    create_proto(protos, output, args.prefix)
