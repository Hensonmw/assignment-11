#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
1 March 2016
Assignment 11 Task 2

A program taking an file and first letter of a word specified by user input
and writing an output file of the specified first letter of the word.
'''
import argparse
import string
from collections import Counter
import os
# from pprint import pprint
# import json this might put the histogram tuple into a file...


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--infile",
        required=True,
        help="""The input file name""",
    )
    parser.add_argument(
        "--FL",
        required=True,
        help="""The first letter of the words you want""",
    )
    return parser.parse_args()


def remove_punct(args):
    with open(args.infile, 'r') as my_input:
        for line in my_input:
            exclude = set(string.punctuation)
            remove_ch = ''.join(ch for ch in my_input if ch not in exclude)
            lower_case = remove_ch.lower()
            replace_data = lower_case.replace('\n', ' ')
            split_data = replace_data.split(' ')
    return(split_data)


def append_file_name(args):
    letter = args.FL.upper()
    new_name = "{}-{}".format(letter, args.infile)
    return new_name


def write_file(args, new_name):
    d = dict(Counter(remove_punct(args)))
    with open(new_name, 'w') as my_output:
        for word, value in iter(sorted(d.items(), key=lambda t: t[1],
        reverse=True)):
            if word.startswith(args.FL.lower()):
                my_output.write("{0:10}\t{1}\n".format(word, value))
            # print("{0}\t{1}\n".format(word, value))


def main():
    args = get_args()
    new_name = append_file_name(args)
    remove_punct(args)
    write_file(args, new_name)


if __name__ == '__main__':
    main()
