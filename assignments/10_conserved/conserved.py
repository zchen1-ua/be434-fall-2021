#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-11-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
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

    lines = []
    for line in args.file:
        print(line, end='')
        lines.append(line.rstrip())

    nchar = len(lines[0])
    nrow = len(lines)

    out_str = ""
    for i in range(nchar):
        common = ""
        for j in range(nrow):
            common = common + (lines[j])[i]
        out_str = out_str + ("|" if len(set(common)) == 1 else "X")
    print(out_str)


# --------------------------------------------------
if __name__ == '__main__':
    main()
