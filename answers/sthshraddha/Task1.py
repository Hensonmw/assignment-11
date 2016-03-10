#!/usr/bin/env python

"""
Assignment_11: Task1
Writing a program to print out, in decreasing order the 20 most common words \
and the count of each word used. The program should contain a main loop and \
an ifmain statement, it should be formatted correctly, and you should use \
argparse to get the name of the input and output files from the user. You may \
use any type of dictionary object in your code. You should print your Top 20 \
results to the screen using the .format() string method, and your results \
should be prettily spaced (again, using .format()) so that the column of words\
and word counts are justified left.

Created by Shraddha Shrestha on March 7, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""


import string
from collections import Counter
import argparse


def parser():
    parser = argparse.ArgumentParser(description='Open input file to count 20\
     most frequent words and puts them in an output file')
    parser.add_argument("-i", "--input", type=str, required=True, help="input \
    text file, make sure to add '-i' before input file name")
    parser.add_argument("-o", "--output", type=str, required=True, help="\
    output tab delimited text file, add '-o' before output file name")
    args = parser.parse_args()
    return args


def remove_punctuation(filename):
    # removing all the possible punctuation marks in the input file
    with open(filename, 'r') as inputfile:
        step1 = inputfile.read().replace("\n", " ").replace(";", " ").replace(","
        , " ").replace(".", " ").replace("(", " ").replace(")", " ").replace("-"
        , " ").replace("'", " ").replace(":", " ").casefold()
        return step1


def counting_words(A, filename):
    # splitting the punctuation removed string file into a list file
    step2 = A.split()
    # Counting all the words in list file
    words_count = Counter(step2)
    with open(filename, 'w') as outputfile:
        for key, value in words_count.items():
            outputfile.write('{0}\t{1}\n'.format(key, value))
    # storing words_count file to be used in "top_20_from_words_count" function
    return words_count


def top_20_from_words_count(B):
    top_20_common_words = B.most_common(20)
    return top_20_common_words


def main():
    arg = parser()
    # argparse command for input file
    input_file = arg.input
    # argparse command for output file
    output_file = arg.output
    first_file = remove_punctuation(input_file)
    second_file = counting_words(first_file, output_file)
    third_file = top_20_from_words_count(second_file)
    print("\nThe top 20 common words in the user input file are:")
    for item in third_file:
        print('{0: <5}\t{1: <5}'.format(item[0], item[1]))
    # this is printing the top 20 words in "justified left" format

if __name__ == '__main__':
    main()
