#!/usr/bin/env python3
"""
Author : Kenneth Schackart <schackartk1@gmail.com>
Date   : 2021-11-08
Purpose: find conserved bases
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seqs = list(map(str.rstrip, args.file.readlines()))

    for seq in seqs:
        print(seq)

    alignment = ''
    for aligned in list(zip(*seqs)):
        alignment += '|' if all(b == aligned[0] for b in aligned) else 'X'

    print(alignment)


# --------------------------------------------------
if __name__ == '__main__':
    main()
