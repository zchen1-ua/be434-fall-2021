#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-11-14
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, encoding='utf-8') as fh:
            args.text = fh.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for seq in args.text.splitlines():
        print(rle(seq))


# --------------------------------------------------
def rle(seq):
    """ Create RLE """

    result = seq[0]
    rep = 1

    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            rep += 1
        else:
            if rep > 1:
                result = result + str(rep)
            result = result + seq[i+1]
            rep = 1

    if rep > 1:
        result += str(rep)
    return result


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
if __name__ == '__main__':
    main()
