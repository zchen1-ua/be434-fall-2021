#!/usr/bin/env python3
"""
Author : zhuochen <zchen1@math.arizona.edu>
Date   : 2021-09-27
Purpose: Concatenate files
"""

import argparse
# import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input files(s)')

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true',
                        default=False)

    # args = parser.parse_args()

    # text = []
    # for file in args.files:
    #     text.append(file.read().rstrip().splitlines())
    # args.files = text

    # return args
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
     
    # for fh in args.files:
    #     line_num = 0
    #     for line in fh:
    #         line_num += 1
    #         if args.number:
    #             print('{:>6}\t{}'.format(line_num, line.rstrip()))
    #         else:
    #             print(line, end='')

         
    for fh in args.files:
        line_num = 0
        for line_num, line in enumerate(fh, start=1):
            if args.number:
                print(f'{line_num:>6}\t{line.rstrip()}')
            else:
                print(line, end='')
    # for file in args.files:
    #     for num, val in enumerate(file, start=1):
    #         if args.number:
    #             print('     ' + f'{num}' + '\t' + f'{val}', end='\n')
    #         else:
    #             print(f'{val}', end='\n')
    # print(args.files)
    # print(type(args.files))
    # print(list(enumerate(args.files)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
