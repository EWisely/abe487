#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) <1 or len(args) >2:
    print('Usage: {} Sequence or filename (length)'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)
filename = args[0]
length = 5
if len(args) ==2:
    length = int(args[1])

#print (length)

if os.path.isfile(filename):
    with open(filename) as file:
        for line in file:
            dna =str(line.rstrip())
            if len(dna) > length:
                print (dna[0:length])
            
else:
    dna = args[0]
    if len(dna) > length:
        print (dna[0:length])

