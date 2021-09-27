#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-09-12
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+', # one or more
                        help='Items to eat')
    
    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items

    if args.sorted: 
        items = sorted(items)
        # items.sort()

    if len(items) == 1:
        print('You are bringing ' + items[0] + '.')
    elif len(items) == 2:
        print('You are bringing ' + ' and '.join(items) + '.')
    else:
        print('You are bringing {}, and {}.'.format(', '.join(items[0:-1]), 
                                                    items[-1]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
