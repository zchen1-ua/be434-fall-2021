#!/usr/bin/env python3
"""
Author : zhuochen <zhuochen@localhost>
Date   : 2021-11-01
Purpose: Rock the Casbah
"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    args = parser.parse_args()

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file:

        basename = os.path.basename(fh.name)
        root, ext = os.path.splitext(basename)

        reader = SeqIO.parse(fh.name, 'fasta')

        i = 1
        for rec in reader:
            if i % 2 != 0:
                outfile = os.path.join(args.outdir, root + '_1' + ext)
            else:
                outfile = os.path.join(args.outdir, root + '_2' + ext)

            out_fh = open(outfile, 'at')
            SeqIO.write(rec, out_fh, 'fasta')
            i += 1

        # i = 1
        # for rec in reader:
        #     if i % 2 != 0:
        #         seq_odd.append(rec)
        #     else:
        #         seq_even.append(rec)
        #     i += 1

        # outfile_odd = os.path.join(args.outdir, root + '_1' + ext)
        # outfile_even = os.path.join(args.outdir, root + '_2' + ext)

        # out_fh_odd = open(outfile_odd, 'wt')
        # out_fh_even = open(outfile_even, 'wt')

        # SeqIO.write(seq_odd, out_fh_odd, 'fasta')
        # SeqIO.write(seq_even, out_fh_even, 'fasta')


# --------------------------------------------------
if __name__ == '__main__':
    main()
