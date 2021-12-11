#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-09-07
Purpose: Add numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('nums',
                        metavar='INT',
                        type=int,
                        nargs='+',
                        help='Numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()

    # nums = []
    # total = 0
    # for num in args.nums:
    #     nums.append(str(num))
    #     total += num

    # print('{} = {}'.format(' + '.join(nums), total))

    # nums = [str(num) for num in args.nums]
    # print('{} = {}'.format(' + '.join(nums), sum(args.numbers)))

    print('{} = {}'.format(' + '.join(map(str, args.nums)), sum(args.nums)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
