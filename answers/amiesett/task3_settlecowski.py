#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 11 Task 3

Amie Settlecowski
8 Mar. 2016

This program outputs a file for each letter with every word beginning with that
letter and its count

python task3_settlecowski.py --i "input_file.txt" --path "\path_to_directory\"
"""


import argparse
import os
import string


def path_arg(parserr):
    ''' requires --path flag for user to indicate path to appropriate directoy'''
    parserr.add_argument("--path",
        required=True,
        help="Path to directory containing this program and input file",
        type=str)


def infile_arg(parserr):
    '''requires --i flag for user to indicate input file name'''
    parserr.add_argument("--i",
        required=True,
        help="Name of input file, including file extension",
        type=str)


def process_line(string, letter_dict):
    '''
    Parse lines from file and add words and their count to dictionary by
    first letter
    '''
    string = string.rstrip()
    first_letter = string[0]
    if first_letter.isalpha():
        string = string.split('\t')
        letter_dict[first_letter][string[0]] = string[1]
    return letter_dict


def print_word_rank(counts, f):
    '''
    Prints and/or writes to file (f) words and their counts
    '''
    keys = counts.keys()
    for index in keys:
        f.write('{0}{2}{1:{3}}{4}'.format(index,
                                            str(counts[index]),
                                            '\t',
                                            '<',
                                            '\n'))


def main():
    # creater Parser object with arguments for path and input/output files
    file_name_parser = argparse.ArgumentParser()
    infile_arg(file_name_parser)
    path_arg(file_name_parser)
    file_name_args = file_name_parser.parse_args()
    path = file_name_args.path
    os.chdir(path)
    in_f = file_name_args.i

    # check that input file opens in read mode w/out error
    with open(in_f, 'r') as ifile:
        if ifile.readable() == 'False':
            ifile.close()
        else:
            pass

        # construct dictionary with each letter as a key to another dictionary
        words_by_letter = {}
        for letter in string.ascii_lowercase:
            words_by_letter[letter] = {}
        for line in ifile:
            words_by_letter = process_line(line, words_by_letter)

        # write results to files by letter
        for letter in string.ascii_lowercase:
            out_f = '{}-words-'.format(letter) + in_f
            ofile = open(out_f, 'w')
            print_word_rank(words_by_letter[letter], ofile)
            ofile.close()

        ifile.close()

if __name__ == '__main__':
    main()
