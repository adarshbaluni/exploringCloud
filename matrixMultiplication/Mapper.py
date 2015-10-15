#!/usr/bin/python
import sys
#BLOCKSIZE must be the intergral power of two
BLOCKSIZE = 128
TOTALSIZE = 1024
#!numbers of blocks for Matrix A/B
NB = (int)(TOTALSIZE/BLOCKSIZE)
#input comes form STDIN
for line in sys.stdin:
#remove leading and trailing whitespace
	line = line.strip()
#parse the input	
	A_B, lineno, row_value = line.split(' ',2)
	if A_B == 'L':
		ib = (int)(lineno)/BLOCKSIZE
		for jb in range(NB):
			#the key is the BLOCK Number
			intermediate_key = "%0.5d"%(ib*NB+jb)
			#the value is the{L/R}:{LineNo}:{vlaues of current line}
			intermediate_value = "L:%s:%s"%(lineno, row_value)
			#key and value are separted by a tab
			#print "%s\t%s"%(intermediate_key,intermedate_value)
			print(intermediate_key+'\t'+intermediate_value)
	if A_B == 'R':
		jb = (int)(lineno)/BLOCKSIZE
		for ib in range(NB):
			intermediate_key = "%0.5d"%(ib*NB+jb)
			intermediate_value = "R:%s:%s"%(lineno, row_value)
			#print "%s\t%s"%(intermediate_key,intermedate_value)
			print(intermediate_key+'\t'+intermediate_value)
	
