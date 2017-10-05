#!/usr/bin/env python3
"""
say hello to the arguments
@author: Eldridge
"""

import sys
if len(sys.argv)<2:
    sys.exit("Usage: "+sys.argv[0]+"NAME [NAME2...]")
elif len(sys.argv)>1:
	names=sys.argv[1:]
	if len(names)==1:
		print ("Hello to the 1 of you: " + sys.argv[1]+ "!")
	if len(names)>1:
		names.insert(-1, "and")
	if len(names)==3:
		print ("Hello to the 2 of you: " +' '.join(names)+"!") 
	if len(names)>3:
		print ("Hello to the " +str(len(sys.argv)-1) + " of you: " + ', '.join(names[0:-1]) + " " + names[-1] +"!")


