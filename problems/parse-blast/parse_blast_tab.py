#!/usr/bin/env python3

import argparse
import os
import sys

def get_args():
    parser = argparse.ArgumentParser(description='Argparse Python script')
    parser.add_argument('file', help='BLAST output file',
                        type=str, metavar='str')
    parser.add_argument("-p", "--pct_id", help='minimum percent identity',
                        type=float, metavar="float", default =0)
    parser.add_argument("-e", "--evalue", help='max E value',
                        type=float, metavar="float", default =1)
    return parser.parse_args()

def main():
    args = get_args()
    file = args.file
    pid = args.pct_id
    maxeval =args.evalue

    if not os.path.isfile(file):
        print('"{}" is not a file'.format(file))
        sys.exit(1)

    fields = 'qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore'.split()
    
    for line in open (file):
        if line.startswith('#'):
            continue
        values = line.rstrip().split('\t')
        rec = dict(zip(fields, values))

        qseqid = rec.get('qseqid')
        sseqid = rec.get('sseqid')
        pident = rec.get('pident')
        evalue = rec.get('evalue')
        
        if float(pident) >= float(pid) and float(evalue) <= float(maxeval): 
            stuff = (qseqid, sseqid, pident, evalue)
            print('\t'.join(stuff))
            
 
if __name__ == '__main__':
    main()
