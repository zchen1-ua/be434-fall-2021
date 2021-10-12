#!/usr/bin/env python3
"""Apples and Bananas"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    new_text = []

    for char in text:

        if char in 'aeiou':
            new_text.append(vowel)
        elif char in 'AEIOU':
            new_text.append(vowel.upper())
        else:
            new_text.append(char)

<<<<<<< HEAD
        print(char, '->', new_text[-1])
=======
        if char == ' ':
            new_text.append('\n')
>>>>>>> 1d289c20a2d4459a215b36ff905206e6e59037e1

    print(''.join(new_text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
