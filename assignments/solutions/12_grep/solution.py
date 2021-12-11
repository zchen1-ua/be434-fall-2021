#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-16
Purpose: Python grep
"""

# pylint:disable=consider-using-f-string

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern', metavar='PATTERN', help='Search pattern')

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
                        help='Output',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    pattern = re.compile(args.pattern, re.I if args.insensitive else 0)
    num_files = len(args.files)

    for fh in args.files:
        for line in filter(pattern.search, fh):
            print('{}{}'.format(fh.name + ':' if num_files > 1 else '', line),
                  end='',
                  file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
