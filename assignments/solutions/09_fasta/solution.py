#!/usr/bin/env python3
"""Split interleaved, paired reads into _1/2 files"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line args"""

    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for fh in args.files:
        # filename = os.path.basename(fh.name)
        # base, ext = os.path.splitext(filename)
        # forward = open(os.path.join(out_dir, base + '_1' + ext), 'wt')
        # reverse = open(os.path.join(out_dir, base + '_2' + ext), 'wt')
        # print('{} -> forward "{}" reverse "{}"'.format(fh.name, forward.name,
        #                                                reverse.name))

        for i, rec in enumerate(SeqIO.parse(fh, 'fasta')):
            is_even = i % 2 == 0
            print(i, is_even, rec.id)
            SeqIO.write(rec, forward if i % 2 == 0 else reverse, 'fasta')

        # for i, rec in enumerate(SeqIO.parse(fh, 'fasta')):
        #     SeqIO.write(rec, forward if i % 2 == 0 else reverse, 'fasta')

    print(f'Done, see output in "{out_dir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
