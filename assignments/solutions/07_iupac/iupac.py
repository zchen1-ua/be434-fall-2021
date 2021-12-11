#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-10-20
Purpose: IUPAC translation of sequence
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='IUPAC translation of sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seqs',
                        metavar='SEQ',
                        nargs='+',
                        help='Input sequence(s)')

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
    # print(args.seqs)
    trans = {
        # 'A': 'A',
        # 'C': 'C',
        # 'G': 'G',
        # 'T': 'T',
        # 'U': 'U',
        'R': '[AG]',
        'Y': '[CT]',
        'S': '[GC]',
        'W': '[AT]',
        'K': '[GT]',
        'M': '[AC]',
        'B': '[CGT]',
        'D': '[AGT]',
        'H': '[ACT]',
        'V': '[ACG]',
        'N': '[ACGT]',
    }

    for seq in args.seqs:
        print(seq,
              ''.join([trans.get(base, '-') for base in seq]),
              file=args.outfile)

    # for seq in args.seqs:
    #     print(seq,
    #           ''.join([trans.get(base, '-') for base in seq]),
    #           file=args.outfile)

    # for seq in args.seqs:
    #     regex = ''.join([trans.get(base, '-') for base in seq])

    #     # regex = ''
    #     # for base in seq:
    #     #     # regex += trans[base] # DON'T DO THIS!
    #     #     regex += trans.get(base, '-')

    #     if '-' in regex:
    #         print(f'Unknown base in "{seq}"', file=sys.stderr)
    #     else:
    #         print(seq, regex, file=args.outfile)

    # if args.outfile != sys.stdout:
    # if args.outfile is not sys.stdout:
    # if args.outfile.name != '<stdout>':
    if os.path.isfile(args.outfile.name):
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
