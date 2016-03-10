#!/usr/bin/env python
# utf-8

"""
Program counts words usage for all english alphabet in output file from" +
" task1
Created by Pramod Pantha on 8 March, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


import os
import argparse


def oppenningfile(filename):
    """
    this program looks through all the alphabet in the word count file" +
    " then makes a list in tab delimited file named as alphabet(a,b..z)-words"
    """
    english_alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in english_alphabet:
        listbyletter = []
    with open(filename, 'r') as my_file:
        for line in my_file:
            if line[0] == letter:
                listbyletter.append(line)
    writefilename = os.path.join(letter+"-words-"+filename)
    with open(writefilename, 'w') as letterfile:
        for value in listbyletter:
            letterfile.write(value)


def parser():
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", required=True,
                        help="Enter '--input_file', space, and then" +
                        " the name of the input file (should be exactly same" +
                        " the name of the output file from task 1)", type=str)
    parser.add_argument("--output_file", required=True,
                        help="Enter '--input_file', space, and then" +
                        " the name of the output file.", type=str)
    args = parser.parse_args()
    return args


def main():
    args = parser()
    input_file = args.input_file
    oppenningfile(input_file)
    result = oppenningfile(input_file)
    print(result)


if __name__ == '__main__':
    main()
