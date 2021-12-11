#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-10-05
Purpose: Find common words
"""

import argparse
import sys
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
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
    words1 = get_words(args.file1)
    words2 = get_words(args.file2)

    for word in words1.keys():
        if word in words2:
            print(word, file=args.outfile)


# --------------------------------------------------
def get_words(fh):
    """ Get all the words from a filehandle """

    words = defaultdict(int)
    for line in fh:
        for word in line.rstrip().split():
            # if word not in words:
            #     words[word] = 1
            words[word] += 1

    return words


# --------------------------------------------------
if __name__ == '__main__':
    main()
