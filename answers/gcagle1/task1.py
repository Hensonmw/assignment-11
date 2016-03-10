#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
1 March 2016
Assignment 11 Task 1

A program taking an file specified by user input and writing an output file
specified by the user of the top 20 most used words. Also prints the words.
'''
import argparse
import string
from collections import Counter
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
        "--outfile",
        required=True,
        help="""The output file name""",
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


def write_file(args):
    count = Counter(remove_punct(args))
    d = dict(count.most_common(20))
    with open(args.outfile, 'w') as my_output:
        for word, value in iter(sorted(d.items(), key=lambda t: t[1],
        reverse=True)):
            my_output.write("{0:10}\t{1}\n".format(word, value))
            print("{0:10}\t{1}".format(word, value))


def main():
    args = get_args()
    remove_punct(args)
    write_file(args)


if __name__ == '__main__':
    main()
