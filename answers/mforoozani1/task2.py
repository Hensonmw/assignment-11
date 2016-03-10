#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2 to Write a program to count word usage in the text
count the most 20 common words use collection module, and argparser
"""
# from collections import Counter
import argparse
import os


def get_parser():
    """
   using argparse to takes the list  as input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputfile", required=True)
    # parser.add_argument("--outputfile", required=True)
    args = parser.parse_args()
    return args


def count_t_words(input_file):
    """
    put T-word in new file with adding T-word to the same path as input
    """
    A = []
    with open(input_file, 'r') as d:
        for i in d:
            if i[0] == "t":
                A.append(i)
    m = os.path.join("T-words-" + input_file)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)


def main():
    args = get_parser()
    inputfile = args.inputfile
    # outputfile = open(args.outputfile, "w")
    count_t_words(inputfile)


if __name__ == '__main__':
    main()
