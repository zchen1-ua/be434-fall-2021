#!/usr/bin/env python3
""" Find conserved bases """

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seqs = list(map(str.rstrip, args.file))
    conserved = []

    for i in range(len(seqs[0])):
        chars = set([seq[i] for seq in seqs])
        # chars = set(map(lambda s: s[i], seqs))
        conserved.append('|' if len(chars) == 1 else 'X')

    print('\n'.join(seqs))
    print(''.join(conserved))


# --------------------------------------------------
if __name__ == '__main__':
    main()
