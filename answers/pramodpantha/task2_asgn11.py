#!/usr/bin/env python
# utf-8

"""
Program counts words usage starting from t in output file from task1
Created by Pramod Pantha on 7 March, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


import os
import argparse


def oppenningfile(filename):
    """
    this program looks the words starting with "t" in the word count file" +
    " then makes a list in tab delimated file named as T-words-output_file_" +
    " task1
    """
    list1 = []
    with open(filename, 'r') as my_file:
        for line in my_file:
            if line[0] == "t":
                list1.append(line)
    writefilename = os.path.join("T-words-" + filename)
    with open(writefilename, 'w') as tfile:
        for value in list1:
            tfile.write(value)


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
    result = oppenningfile(input_file)
    print(result)


if __name__ == '__main__':
    main()
