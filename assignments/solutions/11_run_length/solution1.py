#!/usr/bin/env python3
""" Run-length encoding/data compression """

import argparse
import os
# from itertools import starmap


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        # fh = open(args.text)
        # args.text = fh.read().strip()

        # with open(args.text) as fh:
        #     args.text = fh.read().strip()

        args.text = open(args.text).read().strip()

    return args


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()

    for seq in args.text.splitlines():
        print(rle(seq))


# --------------------------------------------------
def rle(seq):
    """ Create RLE """

    counts = []
    count = 0
    prev = None
    for char in seq:
        # We are at the start
        if prev is None:
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
    for char, num in counts:
        ret += '{}{}'.format(char, '' if num == 1 else num)
    return ret

    # return ''.join(['{}{}'.format(c,
    #     '' if n == 1 else n) for c, n in counts])

    # fmt = lambda c, n: '{}{}'.format(c, '' if n == 1 else n)
    # return ''.join(starmap(fmt, counts))


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
