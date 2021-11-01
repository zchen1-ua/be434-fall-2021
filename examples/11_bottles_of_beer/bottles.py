#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-10-25
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Sing Bottles of Beer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--num "{args.number}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # if args.number < 1:
    #     sys.exit(f'--number "{args.number}" must be greater than 0')

    verses = [verse(n) for n in range(args.number, 0, -1)]
    print('\n\n'.join(verses))


# --------------------------------------------------
def verse(bottle):
    """ Sing a verse """

    next_bottle = bottle - 1
    s1 = '' if bottle == 1 else 's'
    s2 = '' if next_bottle == 1 else 's'
    num_next = 'No more' if next_bottle == 0 else next_bottle
    return '\n'.join([
        f'{bottle} bottle{s1} of beer on the wall,',
        f'{bottle} bottle{s1} of beer,',
        f'Take one down, pass it around,',
        f'{num_next} bottle{s2} of beer on the wall!',
    ])

# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])

# --------------------------------------------------
if __name__ == '__main__':
    main()
