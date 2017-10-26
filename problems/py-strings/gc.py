#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

dna = args[0]

#print('Sequence is "{}"'.format(dna))
i=0
gc =['g','G','c','C']
for base in dna:
    if base in gc:
        i += 1
        
percentage= i/len(dna)*100
print ('{}% GC'.format(int(percentage)))

