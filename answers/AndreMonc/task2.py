# !/usr/bin/env python
# encoding: utf-8


"""
My letter-based file-making program
Created by Andre Moncrieff on 2 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.

Goal of program is to take a massive list of lists (each inner list contains
a pair of words and word counts) and writing the T-words and their word counts
to a new file. I avoid making a dictionary so that I maintain word sorting from
most common to least common.

"""

from collections import Counter
import argparse
import os
from string import ascii_lowercase


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", required=True,
                        help="Enter '--input_file', space, and then" +
                        " the name of the input file (which should be" +
                        " equivalent to name of the output file from task 1)",
                        type=str)
    args = parser.parse_args()
    return args


def word_count_megalist(input_file):
    word_and_count = []
    for line in input_file:
        stripped = line.rstrip("\n")
        split = stripped.split("\t")
        word_and_count.append(split)
    return word_and_count


"""
def make_dict(word_and_count):
    dictionary = {}
    for pair in word_and_count:
        dictionary[pair[0]] = pair[1]
    return dictionary
"""


def parse_and_write(megalist, input_file_name):
    # for letter in ascii_lowercase:
    same_letter = []
    output_file = open("-words-.txt", "w")
    output_file_name = os.path.splitext("-words-.txt")[0]
    letter = "T"
    new_name = "{}{}{}{}".format(letter,
                                 output_file_name,
                                 input_file_name,
                                 ".txt")
    os.rename(output_file.name, new_name)
    # print(new_name)
    for item in megalist:
        letter = "t"
        if item[0][0] == letter:
            same_letter.append(item)
    # print(megalist)
    # print(same_letter)
    for item in same_letter:
        output_file.write("{}{}{}{}".format(item[0], "\t", item[1], "\n"))
    output_file.close()


def main():
    args = parser()
    input_file_1 = open(args.input_file, "r")
    megalist = word_count_megalist(input_file_1)
    input_name = os.path.splitext(input_file_1.name)[0]
    parse_and_write(megalist, input_name)

    """
    for key, value in sorted_dict:
        if str(key[0]) == "a":
        #if key[0] == "a":
            print(key, value)
    """
    input_file_1.close()


if __name__ == '__main__':
    main()
