#!/usr/bin/env python3

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        default=None)

    args = parser.parse_args()

    if args.kmer <= 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words1 = {}
    words2 = {}
    for fh in args.file1:
        for line1 in fh.split():
            for kmer1 in find_kmers(line1, args.kmer):
                print(kmer1)
                if kmer1 not in words1.keys():
                    words1[kmer1] = 0
                words1[kmer1] += 1

    for gh in args.file2:
        for line2 in gh.split():
            for kmer2 in find_kmers(line2, args.kmer):
                print(kmer2)
                if kmer2 not in words2.keys():
                    words2[kmer2] = 0
                words2[kmer2] += 1

    for item in set(words1).intersection(set(words2)):
        print("{:10} {:5} {:5}".format(item,words1[kmer1],words2[kmer2]))



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
