#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 11 Task 2

Amie Settlecowski
8 Mar. 2016

This program parses out and prints to file words that begin with the letter t
and their counts

python task2_settlecowski.py --i "input_file.txt" --path "\path_to_directory\"
"""


import argparse
import os


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


def process_line(string, letter, letter_dict):
    '''
    Parse lines from file for those beginning with letter.
    '''
    if string[0] == letter:
        string = string.rstrip()
        string = string.split('\t')
        letter_dict[string[0]] = string[1]
    return letter_dict


def print_word_rank(counts, f):
    '''
    Prints and/or writes to file (f) words and their counts stored in
    Counter (counts) in descending order.
    '''
    keys = counts.keys()
    for index in keys:
        f.write('{0}{2}{1:{3}}{4}'.format(index,
                                            counts[index],
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

        # construct dictionary that stores words and counts as key, value pairs
        word_counter = {}
        for line in ifile:
            word_counter = process_line(line, 't', word_counter)

        # print and write results to screen and file
        out_f = path + '\T-words-' + os.path.basename(os.path.abspath(in_f))
        ofile = open(out_f, 'w')
        print_word_rank(word_counter, ofile)

        ifile.close()
        ofile.close()

if __name__ == '__main__':
    main()
