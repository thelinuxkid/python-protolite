import os
import re
import argparse
import logging
import itertools

import antlr3

from protolite.parse import proto_parser
from protolite.parse import proto_lexer

log = logging.getLogger(__name__)


ignore_types = [
    proto_parser.OPTION_LITERAL,
    proto_parser.IMPORT_LITERAL,
]


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


def proto_dict(tree, prefix=None):
    if tree is None or tree.getType() in ignore_types:
        return None

    if tree.getType() == proto_parser.PACKAGE_LITERAL:
        # TODO should the package be used as a namespace?
        return None

    children =[]
    for child in tree.getChildren():
        _child = proto_dict(child, prefix)
        if _child:
            children.append(_child)

    # top-level
    if tree.getType() == proto_parser.PROTO:
        return dict(children)

    if tree.getType() in [proto_parser.MESSAGE_LITERAL, proto_parser.ENUM_LITERAL]:
        name = children.pop(0)
        name = to_underscore(name.getText(), prefix=prefix)
        return name, dict(children)

    if tree.getType() == proto_parser.MESSAGE_FIELD:
        # TODO scope = children[0]['text']
        # TODO if field_type.getType() == ProtoParser.IDENTIFIER:
        _, field_type, field_name, field_number = children
        field_type = to_underscore(field_type.getText(), prefix=prefix)
        field_name = to_underscore(field_name.getText(), prefix=prefix)
        field_number = field_number.getText()
        fields = dict([
            ('type', field_type),
            ('name', field_name),
        ])
        return field_number, fields

    if tree.getType() == proto_parser.ENUM_FIELD:
        enum_name, enum_number = children
        enum_name = to_underscore(enum_name.getText(), prefix=prefix)
        enum_number = enum_number.getText()
        return enum_number, enum_name

    return tree


def root_rule(proto):
    stream = antlr3.ANTLRFileStream(proto)
    lexer = proto_lexer.proto_lexer(stream)
    tokens = antlr3.CommonTokenStream(lexer)
    parser = proto_parser.proto_parser(tokens)
    rule = parser.proto()
    return rule.tree


def proto_order(proto):
    dir = os.path.dirname(proto)
    root = root_rule(proto)
    for child in root.getChildren():
        if child.getType() == proto_parser.IMPORT_LITERAL:
            depend, = child.getChildren()
            depend = depend.getText().strip('"')
            depend = os.path.join(dir, depend)
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
        print proto_dict(root, prefix)

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
