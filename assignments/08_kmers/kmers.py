#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-10-25
Purpose: Rock the Casbah
"""

import argparse


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

    # parser.add_argument('file3',
    #                     metavar='FILE2',
    #                     type=argparse.FileType('wt'),
    #                     help='Input file 2')

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    kmers1 = {}
    for line in args.file1:
        for word in line.split():
            for kmer in find_kmers(word, args.kmer):
                if kmer not in kmers1:
                    kmers1[kmer] = 0
                kmers1[kmer] += 1

    kmers2 = {}
    for line in args.file2:
        for word in line.split():
            for kmer in find_kmers(word, args.kmer):
                if kmer not in kmers2:
                    kmers2[kmer] = 0
                kmers2[kmer] += 1

    common = set(kmers1).intersection(set(kmers2))
    for kmer in common:
        print(f'{kmer:<10} {kmers1[kmer]:>5} {kmers2[kmer]:>5}')


# --------------------------------------------------
def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
