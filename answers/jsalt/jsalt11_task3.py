#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment 11
Task 3 Program: Getting all the letters + counts
Jessie Salter
1 March 2016
"""

import argparse
import os.path
import string


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


def alpha_words(input_file, letter):
    '''Creates a list of all words starting with a given letter and their word
    count'''
    alpha_list = []
    with open(input_file, 'r') as my_file:
        for word in my_file:
            if word[0] == letter:
                alpha_list.append(word)
    return alpha_list


def results_file(results, output):
    '''Creates a new file with the only the t-words and their word counts.
    Don't need to include any formatting because the tabs and linebreaks are
    still there from when we pulled the list from the input file.'''
    with open(output, 'w') as my_file:
        for item in results:
            my_file.write(item)


def main():
    args = prompt()
    alphabet = string.ascii_lowercase
    # Iterating over the alphabet creates a new file for each letter:
    for letter in alphabet:
        alpha_list = alpha_words(args.input, letter)
        # This creates a new file name with the letter name prepended:
        output = os.path.join(str.upper(letter)+'-words-'+args.input)
        results_file(alpha_list, output)


if __name__ == '__main__':
    main()
