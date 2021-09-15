#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-09-15
Purpose: Add numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar='INT',
                        type=int, # force the input to be intergers
                        nargs='+', # one or more
                        help='Numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numbers = args.numbers
    string = [str(n) for n in numbers]

    if len(numbers) == 1:
        print(string[0] + ' = ' + string[0])
    else: 
        print('{} = {}'.format(' + '.join(string), sum(numbers)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
