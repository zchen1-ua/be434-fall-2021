#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-09-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('syllables',
                        metavar='str',
                        nargs='+',
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    solfege = {
        'Do': 'A deer, a female deer',
        'Re': 'A drop of golden sun',
        'Mi': 'A name I call myself',
        'Fa': 'A long long way to run',
        'Sol': 'A needle pulling thread',
        'La': 'A note to follow sol',
        'Ti': 'A drink with jam and bread'
    }

    for note in args.syllables:
        if note in solfege:
            print(note + ', ' + solfege.get(note))
        else:
            print(f'I don\'t know "{note}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
