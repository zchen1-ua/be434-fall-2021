#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-17
Purpose: Rock the Casbah
"""

import argparse
import io
import os
from itertools import zip_longest


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        # args.text = open(args.text).read().rstrip()
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for seq in map(str.rstrip, args.text):
        print(rle(seq))


# --------------------------------------------------
def rle_geeks(message: str) -> str:
    """ Run-length encoding """

    encoded_message = ""
    i = 0

    while (i <= len(message) - 1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message) - 1):
            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        encoded_message = encoded_message + ch + (str(count)
                                                  if count > 1 else '')
        i = j + 1
    return encoded_message


# --------------------------------------------------
def rle_kenny(seq: str) -> str:
    """ Run-length encoding """

    compressed = ''
    last_base = ''
    rep = 1

    for base in seq:
        if base != last_base:
            if rep > 1:
                compressed += str(rep)
            compressed += base
            rep = 1
        else:
            rep += 1
        last_base = base

    if rep > 1:
        compressed += str(rep)

    return compressed


# --------------------------------------------------
def rle_kyc(seq: str) -> str:
    """ Run-length encoding """

    counts = []
    count = 0
    prev = ''
    for char in seq:
        # We are at the start
        if prev == '':
            prev = char
            count = 1
        # This letter is the same as before
        elif char == prev:
            count += 1
        # This is a new char, so record the count
        # of the previous char and reset the counter
        else:
            counts.append((prev, count))
            count = 1
            prev = char

    # get the last char after we fell out of the loop
    counts.append((prev, count))

    ret = ''
    for char, count in counts:
        # ret += char + str(count) if count > 1 else ''
        ret += '{}{}'.format(char, count if count > 1 else '')

    return ret


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('') == ''
    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
if __name__ == '__main__':
    main()
