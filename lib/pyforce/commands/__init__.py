# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from argparse import ArgumentParser
from os import getcwd


def parse_args():
    if len(sys.argv) > 1:
        if sys.argv[1] in _bin:
            return sys.argv[1:]
    parser = ArgumentParser()
    parser.add_argument(
        "-o, --output",
        dest="outputfile",
        default=getcwd() + "/tested_strings.txt",
        help="Tested hash path")
    parser.add_argument(
        "-v, --verbose", dest="verbose", action="store_true", default=False)
    parser.add_argument(
        "-s, --shadow", dest="shadow", action="store_true", default=False, help="Use /etc/shadow file")
    subparsers = parser.add_subparsers(help='Action to execute')
    subparsers.dest = 'action'
    subparsers.required = True
    brute_force_parser = subparsers.add_parser('brute')
    dict_parser = subparsers.add_parser('dict')
    dict_parser.add_argument(
        "--path",
        action="store_true",
        default=False,
        dest="cached",
        help="Dictionary path")
    return parser.parse_args()
