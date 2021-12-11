#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-10-19
Purpose: Find common kmers
"""

import argparse
from typing import Dict, List, NamedTuple, TextIO
# from collections import defaultdict


class Args(NamedTuple):
    """ Command-line arguments """
    file1: TextIO
    file2: TextIO
    k: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return Args(args.file1, args.file2, args.kmer)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    counts1 = count_kmers(args.file1, args.k)
    counts2 = count_kmers(args.file2, args.k)

    for kmer in sorted(set(counts1) & set(counts2)):
        print('{:<10} {:>5} {:>5}'.format(kmer, counts1[kmer], counts2[kmer]))


# --------------------------------------------------
def count_kmers(fh: TextIO, k: int) -> Dict[str, int]:
    """ Count k-mers in file """

    # counts = defaultdict(int)
    counts = {}
    for line in fh:
        for word in line.split():
            for kmer in find_kmers(word, k):
                if kmer not in counts:
                    counts[kmer] = 0
                counts[kmer] += 1

    return counts


# --------------------------------------------------
def find_kmers(seq: str, k: int) -> List[str]:
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def test_find_kmers() -> None:
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
