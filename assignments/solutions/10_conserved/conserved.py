#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-10
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print conserved sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input sequence file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seqs = args.file.read().splitlines()
    # print(seqs)

    # seqs = []
    # for seq in args.file:
    #     seqs.append(seq.rstrip())
    # print(seqs)

    print('\n'.join(seqs))

    conserved = ''
    for i in range(len(seqs[0])):
        bases = []
        for seq in seqs:
            bases += seq[i]

        # if len(set(bases)) == 1:
        #     conserved += '|'
        # else:
        #     conserved += 'X'

        conserved += '|' if len(set(bases)) == 1 else 'X'

    print(conserved)


# --------------------------------------------------
if __name__ == '__main__':
    main()
