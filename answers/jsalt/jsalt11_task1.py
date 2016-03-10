#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment 11
Task 1 Program: Word Counts & Files
Jessie Salter
1 March 2016
"""

import argparse
import re
from collections import Counter


def prompt():
    '''Takes user input'''
    parser = argparse.ArgumentParser(
        description='''Gets the names of input and output files''')
    parser.add_argument(
        "--input",
        required=True,
        help="Enter the name of the input file you would like to work with",
        type=str
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Enter the name of the output file to save results",
        type=str
    )
    return parser.parse_args()


def formatter(input_file):
    '''Imports the contents of the file given by user input and converts them
    to a string. Uses regular expressions to remove punctuation & whitespace.
    Then lowercases each word from the file'''
    with open(input_file, 'r') as doc:
        doc_string = doc.read()
        doc_list = re.split('\W+', doc_string)
        formatted_list = [str.lower(word) for word in doc_list]
    return formatted_list


def wc_dict(doc):
    '''Uses the Counter subclass from the collections module to create a
    dictionary where each word in the doc is a key and the value is the
    number of times it appears in the text.'''
    wc = Counter(doc)
    return wc


def top_twenty(wc_dict):
    '''Creates list with each word:count pair as a list item, allowing it to
    be sorted from highest to lowest occurrence. Prints the top twenty words in
    order from most used to least.'''
    wc_list = []
    for word, count in wc_dict.items():
        wc_list.append([count, word])
    final_list = sorted(wc_list, reverse=True)
    for item in final_list[:20]:
        print('{0:<12}{1:<3}'.format(item[1], item[0]))
    return final_list


def result_file(results, output):
    '''Creates an output file (names with user input) of every word and its
    count from the original input file.'''
    with open(output, 'w') as my_file:
        for item in results:
            my_file.write('{0}\t{1}\n'.format(item[1], item[0]))


def main():
    args = prompt()
    formatted = formatter(args.input)
    word_count = wc_dict(formatted)
    final_list = top_twenty(word_count)
    result_file(final_list, args.output)


if __name__ == '__main__':
    main()
