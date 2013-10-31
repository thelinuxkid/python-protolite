import os
import argparse
import itertools
import logging

from protolite import generator, util


def parse_args():
    parser = argparse.ArgumentParser(
        description='create alternate Python protobuf files',
    )
    parser.add_argument(
        'protos',
        help='path(s) to the protocol buffer definition file(s)',
        metavar='PATH',
        nargs='+',
        action='append',
        type=str,
    )
    parser.add_argument(
        'output',
        help='path to the directory in which to store the results',
        metavar='PATH',
        type=str,
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
        help='output DEBUG logging statements (default: %(default)s)',
    )
    parser.add_argument(
        '--prefixes',
        help='prefixes to remove from protobuf names',
        nargs='+',
        action='append',
        type=str,
        default=[],
    )
    return parser.parse_args()


def flatten_args(args):
    args = itertools.chain(*args)
    args = [arg.rstrip(',') for arg in args]
    return args


def main():
    args = parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format='%(asctime)s.%(msecs)03d %(name)s: %(levelname)s: %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S',
    )
    protos = flatten_args(args.protos)
    protos = [util.abs_path(proto) for proto in protos]
    output = util.abs_path(args.output)
    if not os.path.exists(output):
        os.mkdir(output)
    prefixes = flatten_args(args.prefixes)
    generator.generate(protos, output, prefixes)
