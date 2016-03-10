#!/usr/bin/env python

"""
Assignment_11: Task2
Write a program that uses argparse to get the name of the tab-delimited file \
you created above from the user. Read that file into your program, and \
determine count of all words that start with the letter "t" (or "T"). \
Using the os.path module, write these t-starting words to a new tab-delimited \
file that has the same name as the input file, but with "T-words" prepended to\
the input filename. For example, if the input filename is \
"all-word-counts.txt", then your output file of t-words should be \
"T-words-all-word-counts.txt". You can accomplish these filename manipulations\
using the os.path module. Your program should contain a main loop and an \
ifmain statement, and it should be formatted correctly.

Created by Shraddha Shrestha on March 7, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""


import argparse
import os


def parser():
    parser = argparse.ArgumentParser(description='Open input file to give an \
    expected output')
    parser.add_argument("-i", "--input", type=str, required=True, help="output \
    text file of Task1.py, make sure to add '-i' before input file name")
    # parser.add_argument("-o", "--output", type=str, required=True, help="\
    # output tab delimited text file, add '-o' before output file name")
    args = parser.parse_args()
    return args


def counting_words_for_input_letter(filename, char='x'):
    my_list = []
    # counting words that starts with any letter in an alphabet
    with open(filename, 'r') as inputfile:
        for letter in inputfile:
            # is at start of line starts with a given alphabet then...
            if letter[0] == char:
                my_list.append(letter)
        return my_list


def creating_output(A, filename):
    with open(filename, 'w') as outputfile:
        for item in A:
            outputfile.write(item)


def main():
    arg = parser()
    file1 = counting_words_for_input_letter(arg.input, char='t')
    file2 = os.path.join('T-words-'+arg.input)
    creating_output(file1, file2)


if __name__ == '__main__':
    main()
