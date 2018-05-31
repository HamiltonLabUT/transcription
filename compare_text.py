# compare_text.py
# 
# Liberty Hamilton 2018
# 

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
import itertools
import sys
import string

def compare_text(text_file1, text_file2):
	'''
	Compare the contents of text_file1 and text_file2 (assuming these are both
	plain text transcription files).  Ignores all whitespace, line breaks, and punctuation,
	as well as {NS} tags ("noise" in transcriptions)
	
	Inputs
	------
	text_file1: [str] 	Path to text file 1
	text_file2: [str]	Path to text file 2

	Outputs
	-------
	Prints out a plain text table with *** in front of lines that differ

	'''
	with open(text_file1) as f:
		print("Loading data from %s"%(text_file1))
		arr1 = list(map(str.split, f))
		t1 = list(itertools.chain.from_iterable(arr1)) 
		print("Getting rid of punctuation and setting all words to uppercase")
		t1 = [t.upper().translate(t.maketrans('','',string.punctuation)) for t in t1 if t!='{NS}' and t!='{BR}']

	with open(text_file2) as f:
		print("Loading data from %s"%(text_file2))
		arr2 = list(map(str.split, f))
		t2 = list(itertools.chain.from_iterable(arr2))
		print("Getting rid of punctuation and setting all words to uppercase")
		t2 = [t.upper().translate(t.maketrans('','', string.punctuation)) for t in t2 if t!='{NS}' and t!='{BR}']

	# Find the maximum length of the longest word in file1
	len1=0
	for t in t1:
		if len(t)>len1:
			len1 = len(t)
	

	# If the left side of the table is going to be longer than the right
	if len(t1)>len(t2):
		for idx, line1 in enumerate(t1):
			if idx<len(t2):
				if line1 != t2[idx]: # If the lines don't match
					print("***", end='')
				if len(line1)<len1:
					# Add offset spaces so that left columns are the same width
					offset = " "*(len1-len(line1))
				else:
					offset = ""
				print(line1 + offset + "\t|\t", t2[idx])
			else:
				print(line1 + offset + "\t|\t")
	# If the right side is longer, or if they're equal
	else:
		for idx, line2 in enumerate(t2):
			if idx<len(t1):
				if t1[idx] != line2: # If the lines don't match
					print("***", end='')
				if len(t1[idx])<len1:
					# Add offset spaces so that left columns are the same width
					offset = " "*(len1-len(t1[idx]))
				else:
					offset = ""
				print(t1[idx] + offset + "\t|\t", line2)
			else:
				offset = " "*len1
				print(offset + "\t|\t", line2)


if __name__ == "__main__":
	compare_text(sys.argv[1], sys.argv[2])
