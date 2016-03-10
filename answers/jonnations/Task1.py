#!/usr/bin/env python
# utf-8

"""
Assignment 11, Task 2
Jon Nations on 4 March 2016
"""
import argparse
import operator
from collections import Counter
import re


def file_in():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, type=str, help="give input file")
    parser.add_argument('--output', required=True, help='give output file')
    args = parser.parse_args()
    return args


def chapter(args):
    with open(args.input, 'r') as mychuck:
        clean = mychuck.read()
        clean = re.sub('\s+', ' ', clean)  # condense all whitespace
        clean = re.sub('[^A-Za-z ]+', '', clean)  # remove non-alpha chars
        # regular expressions from gist.github.com/bradmontgomery
        clean_chuck = clean.split()
        my_dict = {}
        for item in clean_chuck:
            my_dict[item] = clean_chuck.count(item)
        return my_dict


def ordered(c_dict, n=20):
    # sorts the dictionary by occurances, then prints
    # the top 10 most-used words
    chuck_count = Counter(c_dict)
    print("The Top {0} words".format(n))
    for word, count in chuck_count.most_common(n):
        print("{:<7s}{:>7d}".format(word, count))


def out_file(args, c_dict):
    all_count = Counter(c_dict)
    with open(args.output, 'w') as out:
        for key, value in all_count.items():
            out.write("{}\t{}\n".format(key, value))


def main():
    file_in()
    args = file_in()
    chapter(args)
    c_dict = chapter(args)
    ordered(c_dict)
    out_file(args, c_dict)


if __name__ == '__main__':
    main()
