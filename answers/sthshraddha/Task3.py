#!/usr/bin/env python

"""
Assignment_11: Task3
Getting the t-words is all good, but your boss wants you to output a separate \
file for words that start with all letters of the alphabet. So, modify your \
program from Task 2 to output 26 files, the names of which should begin with \
the appropriate letter of the alphabet.

Created by Shraddha Shrestha on March 7, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""
import argparse
import os
import string


def parser():
    parser = argparse.ArgumentParser(description='Open input file to give an \
    expected output')
    parser.add_argument("-i", "--input", type=str, required=True, help="output \
    text file of Task1.py, make sure to add '-i' before input file name")
    # parser.add_argument("-o", "--output", type=str, required=True, help="\
    # output tab delimited text file, add '-o' before output file name")
    args = parser.parse_args()
    return args


def counting_alphabet_words(filename, alphabet):
    # filename is import file name and alphabet is an argument
    my_list = []
    # this will count the frequency of all words in input text file
    with open(filename, 'r') as inputfile:
        for word in inputfile:
            if word[0] == alphabet:
                my_list.append(word)
        return my_list


def creating_final_output(A, filename):
    # filename here is the output file name
    with open(filename, 'w') as outputfile:
        for item in A:
            outputfile.write(item)


def main():
    arg = parser()
    all_alphabet = string.ascii_lowercase
    # string.ascii_lowercase imports all 26 alphabets
    inputfile = arg.input
    for letter in all_alphabet:
        all_list = counting_alphabet_words(inputfile, letter)
        new_list = os.path.join(letter + '-words-'+arg.input)
        creating_final_output(all_list, new_list)


if __name__ == '__main__':
    main()
