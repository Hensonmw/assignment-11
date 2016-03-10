#!/usr/bin/env python
# encoding: utf-8

"""
 My third task for Assignment 11 where a user inputs a text file from which words representing each letter of the alphabet are compiled into their own dictionary. Each dictionary output is printed into a new, tab-delineated text file...giving a total of 26 files (one per letter in alphabet).

 Created by A.J. Turner on March 1, 2016. Helpful instructions/hints provided by S. Shakya.
 Copyright 2016 A.J. Turner. All rights reserved.

"""

import argparse
import re
import os.path
import string


def user_files():
	""" adding user input that includes the name of the file to read and the name of the output file they write"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--file_in", help="Type into command line: --file_in <file name you wish to read>", type=str)
	args = parser.parse_args()
	return args


def all_letters(file,letter):
	""" separating words in input file by alphabetic letter and keeping associated counts"""
	#alphabetically grouped word\tcount lists
	get_letter = re.findall(r'\b['+letter+']\w+\t\d+', file)
	lets = {} #dictionary placeholder for below
	for word_num in get_letter: #iterate over each word in alphabetic list grouping
		split_word = word_num.split('\t')
		lets[split_word[0]] = split_word[1]#creating dictionary with word/count\
		#for each alphabetic group
	return lets


def main():
	args = user_files()
	with open(args.file_in, 'r') as file_in:
		f = file_in.read()
		file_in.close()
		alphabet = list(string.ascii_lowercase) #getting all letts of alphabet as list
		for letter in alphabet: #iterating over the alphabet, one letter at a time
			lets = all_letters(f, letter) #calling dictionaries from function two
			out_file = os.path.join(os.getcwd(), letter.upper()+'-words-'+args.file_in)
			with open(out_file, 'w') as out_file:
			#putting dictionary for each word grouping into a file
				for key,value in lets.items():
					out_file.write("{}\t{}\n".format(key, value))
				out_file.close()	


if __name__ == '__main__':
	main()