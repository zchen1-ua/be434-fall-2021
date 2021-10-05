#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence to translate')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    codon_table = {}
    for line in args.codons:
        key, value = line.rstrip().split()
        codon_table[key] = value

    k = 3
    seq = args.sequence.upper()
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        args.outfile.write(codon_table.get(codon, '-'))

    print('Output written to "{}".'.format(args.outfile.name))


# --------------------------------------------------
if __name__ == '__main__':
    main()
