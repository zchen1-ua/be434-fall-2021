#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-10-11
Purpose: Find common words
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('file2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')

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
    file1 = set(args.file1.read().rstrip().split())
    file2 = set(args.file2.read().rstrip().split())
    common = file1.intersection(file2)
    for word in common:
        print(word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
