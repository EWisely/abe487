#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} file'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

filename = (args[0])
gc =['g','G','c','C']

if os.path.isfile(filename):
    with open(filename) as file:
        for line in file:
            i=0
            dna =str(line.rstrip())
            if not len(dna)==0:
                for base in dna:
                    if base in gc:
                        i += 1
            percentage= i/len(dna)*100
            #print (len(dna))
            print ('{}'.format(int(percentage)))
else:
    print('"{}" is not a file'.format(os.path.basename(sys.argv[1])))
    sys.exit(1)