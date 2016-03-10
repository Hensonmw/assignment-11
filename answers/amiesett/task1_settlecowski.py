#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 11 Task 1

Amie Settlecowski
8 Mar. 2016

This program identifies each word and its number of occurrences from text read
in from a file using and prints to screen/writes to file the results in
descending order

python task1_settlecowski.py --i "input_file.txt" --path "path_to_directory\"
--o "output_file.txt"
"""


from collections import Counter
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


def outfile_arg(parserr):
    ''' requires --o flag for user to indicate output file name'''
    parserr.add_argument("--o",
        required=True,
        help="Name of output file, including file extension",
        type=str)


def process_line(string):
    '''
    Parse line from file by spaces into a list of every word in that line
    '''
    string = string.lower().replace("\r\n", " ").replace("-", " ")
    new_string = ''
    for character in string:
        if character.isalpha() or character == ' ':
            new_string += character
        else:
            pass
    list_of_words = new_string.split(' ')
    return list_of_words


def count_words(word_list, counts):
    '''
    If a word in word_list is not in Counter (counts) it is added as a new key
    with a value of 1. Otherwise, occurrences of each word in word_list is
    added to counts.
    '''
    for word in word_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def print_word_rank(counts, f):
    '''
    Prints and/or writes to file (f) words and their counts stored in
    Counter (counts) in descending order.
    '''
    width = len(max(counts, key=len))
    rank_counts = counts.most_common(len(counts.items())-1)
    n = 0
    for index in rank_counts:
        f.write('{0}{2}{1:{3}}{4}'.format(index[0], index[1],
                                        '\t', '<', '\n', width=width))
        if n < 20:
            print('{0:{3}{width}}{2}{1:{3}}'.format(index[0], index[1],
                                                    '\t', '<', width=width))
        n += 1


def main():
    # creater Parser object with arguments for path and input/output files
    file_name_parser = argparse.ArgumentParser()
    infile_arg(file_name_parser)
    outfile_arg(file_name_parser)
    path_arg(file_name_parser)
    file_name_args = file_name_parser.parse_args()
    path = file_name_args.path
    os.chdir(path)
    in_f = file_name_args.i
    out_f = file_name_args.o

    # check that input file opens in read mode w/out error
    with open(in_f, 'r') as ifile:
        if ifile.readable() == 'False':
            ifile.close()
        else:
            pass

        # construct Counter that stores words and counts as key, value pairs
        word_counter = Counter()
        for line in ifile:
            words = process_line(line)
            word_counter = count_words(words, word_counter)

        # print and write results to screen and file
        ofile = open(out_f, 'w')
        print_word_rank(word_counter, ofile)

        ifile.close()
        ofile.close()

if __name__ == '__main__':
    main()
