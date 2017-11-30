#!/usr/bin/env python3
"""
add thing 1 and thing 2
@author: Eldridge
"""

import sys
if len(sys.argv)!=3:
    sys.exit("Usage: "+sys.argv[0]+" ARG1 ARG2")
elif len(sys.argv)==3:
    things=sys.argv[1:]
    thing1= things[0]
    thing2 =things[1]
    if thing1.isdigit() and thing2.isdigit():
        print (int(thing1)+int(thing2))
    if thing1.isalpha() and thing2.isalpha():
        print (thing1 +' and ' +thing2)	
    else:
        print ('Cannot combine number and string')
