#!/usr/bin/env python
# encoding: utf-8

"""
 My first task for Assignment 11 that has a user input a text file that will have each unique word tallied up and printed into a new, tab-delineated text file along with its usage. Additionally, the top twenty words used from the orginal text file were printed to the screen. 

 Created by A.J. Turner on March 1, 2016. Helpful instructions/hints provided by S. Shakya.
 Copyright 2016 A.J. Turner. All rights reserved.

"""

from collections import Counter

import argparse


def user_input():
	""" adding user input that includes the name of the file to read and the name of the output file they write"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--file_in", help="Type into command line: --file_in <file name you wish to read>", type=str)
	parser.add_argument("--file_out", help="Type into command line: --file_out <file name you wish to write>", type=str)
	args = parser.parse_args()
	return args
	

def easy_count(file,all=True,n=20):
	#get rid of all punctuation, make letters lowercase
	text_in = file.lower().replace("\n", " ").replace("  ", " ").replace("'", "")\
	.replace(",", ""). replace("\t", "").replace (".", "").replace(";", "")\
	.replace(":", "").replace("(", "").replace(")", "")\
	.replace("!", "").replace("?", "").strip().split(" ")
	#print(text_in) #to check formatting before using Counter
	if all == True:
		count_it = Counter(text_in)
	else:
		count_it = Counter(text_in).most_common(n) #gets top n words, where n is a number
	return count_it


def main():
	args = user_input()
		
	#open file that user inputs as read only
	with open(args.file_in, 'r') as file_in:
		f = file_in.read() #reads file
		top20 = easy_count(f,all=False) #only gets top 20 words in text		
		all_words = easy_count(f) #getting all words in text
		file_in.close() #closing file the user input
	print(all_words)
	#open and create a new file with specified name user gave
	with open(args.file_out, 'w') as file_out:
		for key,value in all_words.items(): #iterate through all words and printing them into a file
			file_out.write("{}\t{}\n".format(key, value)) #tab delineated format
		file_out.close() #closes user's file that was created
	
	for word in top20:
		print("{}\t{}".format(word[0], word[1])) #printing top 20 words from original file to screen


if __name__ == '__main__':
	main()
	