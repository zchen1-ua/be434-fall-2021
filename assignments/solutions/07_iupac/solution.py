#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-10-12
Purpose: Expand IUPAC codes
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequences',
                        metavar='SEQ',
                        nargs='+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    trans = {
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

    # f = lambda base: trans.get(base, '-')
    # def f(base): trans.get(base, '-')

    for seq in args.sequences:
        # regex = ''
        # for base in seq:
        #     regex += trans.get(base, base)

        # regex = ''.join([trans.get(base, base) for base in seq])

        # regex = ''.join(map(lambda base: trans.get(base, '-'), seq))
        # regex = ''.join(map(f, seq))
        regex = ''.join(map(trans.get, seq))

        print(f'{seq} {regex}', file=args.outfile)

    outname = args.outfile.name
    if outname != '<stdout>':
        print(f'Done, see output in "{outname}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
