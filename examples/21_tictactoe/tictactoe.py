#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-11-08
Purpose: Rock the Casbah
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='State of the board',
                        metavar='str',
                        type=str,
                        default='.'*9)

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        choices='XO',
                        metavar='player',
                        type=str)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='cell',
                        type=int,
                        choices=range(1, 10),
                        default=None)

    args = parser.parse_args()

    # chars_ok = [c in 'XO.' for c in args.board]
    # if not (len(args.board) == 9 and all(chars_ok))

    if not re.match('^[.XO]{9}$', args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error('Must provide both --player and --cell')

    if args.player and args.cell and args.board[args.cell - 1] in 'XO':
        parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    board = list(args.board)

    if args.player and args.cell:
        board[args.cell - 1] = args.player
        
    print(format_board(board))
    winner = find_winner(board)
    print(f'{winner} has won!' if winner else 'No winner.')


# --------------------------------------------------
def format_board(board):
    """Format the board"""

    cells = [str(i) if c == '.' else c for i, c in enumerate(board, start=1)]
    dashes = "-------------"
    cells_tmpl = '| {} | {} | {} |'
    return '\n'.join([
        dashes,
        cells_tmpl.format(cells[0], cells[1], cells[2]), dashes,
        cells_tmpl.format(cells[3], cells[4], cells[5]), dashes,
        cells_tmpl.format(cells[6], cells[7], cells[8]), dashes
    ])


# --------------------------------------------------
def find_winner(board):
    """Return the winner"""

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for player in ['X', 'O']:
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player


# --------------------------------------------------
if __name__ == '__main__':
    main()
