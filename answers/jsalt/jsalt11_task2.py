#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment 11
Task 2 Program: Getting the T-words
Jessie Salter
1 March 2016
"""

import argparse
import os.path


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
    return parser.parse_args()


def t_words(input_file):
    '''Creates a list of all words starting with t and their word count'''
    t_list = []
    with open(input_file, 'r') as my_file:
        for word in my_file:
            if word[0] == 't':
                t_list.append(word)
    return t_list


def results_file(results, output):
    '''Creates a new file with the only the t-words and their word counts.
    Don't need to include any formatting because the tabs and linebreaks are
    still there from when we pulled the list from the input file.'''
    with open(output, 'w') as my_file:
        for item in results:
            my_file.write(item)


def main():
    args = prompt()
    t_list = t_words(args.input)
    # This creates a new file name and path for the output file:
    output = os.path.join('T-words-'+args.input)
    results_file(t_list, output)


if __name__ == '__main__':
    main()
