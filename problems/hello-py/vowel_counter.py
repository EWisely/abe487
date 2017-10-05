#!/usr/bin/env python3
"""count the vowels in a word"""

import sys
if len(sys.argv)==2:
	word=str(sys.argv[1])
	vowels="aeiouAEIOU"
	n=0
	for letter in word:
		if letter in vowels:
			n=n+1
	#print(n) #works!
	if n ==1:
		print("There is 1 vowel in " + '"' + word +'."')
	else:
		print ("There are "+ str(n) + " vowels in " + '"'+ word +'."')

elif len(sys.argv)<2 or len(sys.argv)>2:
	sys.exit("Usage: "+sys.argv[0]+" STRING")
