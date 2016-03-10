#!/usr/bin/env python
# encoding: utf-8

"""
 My second task for Assignment 11 where a user inputs a text file and the count of all words starting with a 't' will be completed. The output is printed into a new, tab-delineated text file.

 Created by A.J. Turner on March 1, 2016. Helpful instructions/hints provided by S. Shakya.
 Copyright 2016 A.J. Turner. All rights reserved.

"""

import argparse
import re
import os.path


def user_files():
	""" adding user input that includes the name of the file to read and the name of the output file they write"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--file_in", help="Type into command line: --file_in <file name you wish to read>", type=str)
	args = parser.parse_args()
	return args


def all_t(t):
	""" getting all t words from input file, along with associated counts"""
	get_t = re.findall(r'\b[t]\w+\t\d+', t) #find all words beginning with 't' \
	#and their values based on \t (tab-delineated)formatting
	#print(get_t) #to check program
	t_dict = {} #dictionary placeholder for below
	for word_num in get_t:
		split_word = word_num.split('\t')
		#print(split_word) to check that words/values were split
		t_dict[split_word[0]] = split_word[1]#creating dictionary 
	return t_dict
	


def main():
	args = user_files()
	with open(args.file_in, 'r') as file_in:
		f = file_in.read()
		t = all_t(f)
		file_in.close()
	#naming output file to same path as input file
	out_file = os.path.join(os.getcwd(), "T-words-"+args.file_in)
		
	with open(out_file, 'w') as out_file:
		for key,value in t.items(): #iterate through t_dict and printing dict items into a file
			out_file.write("{}\t{}\n".format(key, value)) #tab delineated format
		out_file.close() #closes user's file that was created
	

if __name__ == '__main__':
	main()