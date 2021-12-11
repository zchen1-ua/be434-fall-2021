#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-10-13
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

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

    # words1 = {}
    # for line in args.file1:
    #     for word in line.split():
    #         words1[word] = 1

    # words2 = {}
    # for line in args.file2:
    #     for word in line.split():
    #         words2[word] = 1

    words1 = set()
    for line in args.file1:
        for word in line.split():
            words1.add(word)

    words2 = set()
    for line in args.file2:
        for word in line.split():
            words2.add(word)

    # words1 = args.file1.read().split()
    # words2 = args.file2.read().split()

    # print('\n'.join(words1.intersection(words2)))
    print('\n'.join(words1 & words2))

    for word in words1:
        if word in words2:
            print(word, file=args.outfile)



# --------------------------------------------------
if __name__ == '__main__':
    main()
