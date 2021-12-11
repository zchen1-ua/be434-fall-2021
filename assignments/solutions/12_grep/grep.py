#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-24
Purpose: Rock the Casbah
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='A positional argument')

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_files = len(args.files)

    #
    # Version 1
    #
    # for fh in args.files:
    #     for line in fh:
    #         if re.search(args.pattern, line,
    #                      re.IGNORECASE if args.insensitive else 0):

    #             # print('{}{}'.format(f'{fh.name}:' if num_files > 1 else '',
    #             #                     line),
    #             #       end='',
    #             #       file=args.outfile)

    #             args.outfile.write('{}{}'.format(
    #                 f'{fh.name}:' if num_files > 1 else '', line))

    #
    # Version 2: compile regex
    #
    pattern = re.compile(args.pattern,
                         re.IGNORECASE if args.insensitive else 0)

    for fh in args.files:
        for line in fh:
            if pattern.search(line):
                args.outfile.write('{}{}'.format(
                    f'{fh.name}:' if num_files > 1 else '', line))


    #
    # Version 3: filter
    #
    # pattern = re.compile(args.pattern,
    #                      re.IGNORECASE if args.insensitive else 0)

    # for fh in args.files:
    #     for line in filter(pattern.search, fh):
    #         args.outfile.write('{}{}'.format(
    #             f'{fh.name}:' if num_files > 1 else '', line))


# --------------------------------------------------
if __name__ == '__main__':
    main()
