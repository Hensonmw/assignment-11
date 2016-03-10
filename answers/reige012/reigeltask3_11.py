#!/usr/bin/env python
# encoding: utf-8

"""
This program uses argparser module to import a file containing a list, then
it finds all of the list items in the first index position (i.e. the words)
that begin with the letter with each different letter of the alphabet and it
puts them into a new list with their count values and puts this new list into a
file with the same name as the original input file that has been appended to
match its beginning letter.

Edited by Alicia Reigel. 7 March 2016.
Copyright Alicia Reigel. Louisiana State University. 7 March 2016. All
rights reserved.

"""


import argparse
import os
import string


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


def sort_by_letter(letter, a_file):
    """sorts words that start with 'letter' into their own list"""
    list_words = []
    with open(a_file, 'r') as some_list:
        for a_pair in some_list:
            if a_pair[0] == letter:
                list_words.append(a_pair)
        return list_words


def print_letter_words_to_new_file(a_list, output_file_new):
    """Creates a new file for the list of words beginning with each letter"""
    with open(output_file_new, 'w') as the_final_file:
        for item in a_list:
            the_final_file.write('{}'.format(item))


def main():
    args = parser_obtain_file_names()
    all_letters = string.ascii_lowercase
    # this string method defines all english lowercase alphabet letters
    for letter in all_letters:
        # iterates over each alphabet letter and completes the following:
        new_output_file = os.path.join(str.upper(letter)+'-words-'+args.input)
        # makes a new output file with that letter (capitalized) as the start
        letter_list = sort_by_letter(letter, args.input)
        # sends each letter and the original input file to the sort_by_letter function
        print_letter_words_to_new_file(letter_list, new_output_file)
        # sends the list of words starting with that letter to the print_letter_words_to_new_file

if __name__ == '__main__':
    main()
