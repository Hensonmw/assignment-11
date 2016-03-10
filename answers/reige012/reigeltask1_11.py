#!/usr/bin/env python
# encoding: utf-8

"""
This program uses argparser module to import a text file, then counts the
number of times each word is used in the file and prints those results to an
output file. It also prints the top 20 most used words to the screen.

Edited by Alicia Reigel. 7 March 2016.
Copyright Alicia Reigel. Louisiana State University. 7 March 2016. All
rights reserved.

"""


import argparse
from collections import Counter
import re


def parser_file_input():
    """Function takes a file as input and asks for a name for output file"""
    parser = argparse.ArgumentParser(
            description="""Input a file to use and an output file name"""
            )
    parser.add_argument(
                '--input',
                required=True,
                type=str,
                help='Enter the name of the file containing text.'
            )
    parser.add_argument(
                '--output',
                required=True,
                type=str,
                help='Enter the name of the file containing text.'
            )
    return parser.parse_args()


def clean_up_string(a_string):
    """removes the punctuation from text and splits each word into a list"""
    clean_string = re.sub('[^A-Za-z0-9]+', ' ', a_string)
    # substitutes spaces for almost all punctuation or special characters
    the_new_list = clean_string.replace('?', ' ').replace('  ', '').casefold().split(' ')
    # subs spaces for ?, replaces 2 spaces with 1, lowers case and splits
    return the_new_list


def make_and_count(some_list):
    """creates a dictionary key=word and value=# of times words is used"""
    count_dict = Counter(some_list)
    return count_dict


def get_top_20(a_counted_dictionary):
    """obtains the top 20 words in the text based on the dictionary values"""
    top_count = a_counted_dictionary.most_common(20)
    return top_count


def main():
    args = parser_file_input()
    with open(args.input, 'r') as thats_the_file:
        # access the input file to use for the following:
        data = thats_the_file.read()
        words_list = clean_up_string(data)
        counted_dict = make_and_count(words_list)
        top_20 = get_top_20(counted_dict)
        print('The most common 20 words in the text are:')
        for item in top_20:
            # iterate over the top 20 list to print them in tab-delimit format
            print('{}\t{}'.format(item[0], item[1]))
    with open(args.output, 'w') as output_file:
        for key, value in counted_dict.items():
            output_file.write('{}\t{}\n'.format(key, value))
            # write all keys and values in correct format into output file

if __name__ == '__main__':
    main()
