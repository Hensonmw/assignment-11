#!/usr/bin/env python
# encoding: utf-8

"""
This program uses argparser module to import a file containing a list, then
it finds all of the list items in the first index position (i.e. the words)
that begin with the letter 't' and it puts them into a new list with their
count values and puts this new list into a file with the same name as the
original input file that has been appended to indicate it is for t words only.

Edited by Alicia Reigel. 7 March 2016.
Copyright Alicia Reigel. Louisiana State University. 7 March 2016. All
rights reserved.

"""


import argparse
import os


def parser_obtain_file_names():
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
    return parser.parse_args()


def sort_by_letter_t(a_file):
    t_list_words = []
    with open(a_file, 'r') as some_list:
        for a_pair in some_list:
            if a_pair[0] == 't':
                t_list_words.append(a_pair)
        return t_list_words


def print_t_words_to_new_file(a_list, output_file_new):
    with open(output_file_new, 'w') as the_final_file:
        for item in a_list:
            the_final_file.write('{}'.format(item))


def main():
    args = parser_obtain_file_names()
    t_list = sort_by_letter_t(args.input)
    new_output_file = os.path.join('T-words-'+args.input)
    print_t_words_to_new_file(t_list, new_output_file)


if __name__ == '__main__':
    main()
