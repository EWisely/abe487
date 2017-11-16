#!/usr/bin/env python3

import argparse
import os
import sys
from Bio import SeqIO

def get_args():
    parser = argparse.ArgumentParser(description='FASTA trimmer')
    parser.add_argument('file' , metavar ='fasta_file', help='FASTA file',
                        type=str, default='foo')
    parser.add_argument('-s', '--start', help='start position',
                        metavar='int', type=int, default=0)
    parser.add_argument('-e', '--end', help='end position',
                        metavar='int', type=int, default=None)
    parser.add_argument('-m', '--min', help='minimum length',
                        metavar='int', type=int, default=0)
    parser.add_argument('-o', '--outfile', help='output file',
                        metavar='str', type=str, default='')
    return parser.parse_args()

def main():
    args = get_args()
    file  = args.file
    start_pos =args.start
    end_pos = args.end
    min_len = args.min
    outfile =args.outfile

    if start_pos > 0:
        start_pos -=1

    if len(outfile) == 0:
        outfile = file + '.trimmed'

    out_fh = open(outfile, 'w')

    num_taken = 0

    with open(file) as fh:
        for record in SeqIO.parse(fh, "fasta"):
            seq =str(record.seq[start_pos:end_pos])
            if len(seq) >= min_len:
                num_taken += 1
                out_fh.write('\n'.join(['>' + record.id, seq, '']))
    print('Wrote {} sequence{} to "{}"'.format(num_taken, 
                                               '' if num_taken == 1 else 's',
                                               outfile))
if __name__ == '__main__':
    main()
