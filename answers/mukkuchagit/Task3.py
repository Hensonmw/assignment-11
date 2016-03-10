#!/usr/bin/env python
# encoding: utf-8
"""
Files; assignment 11.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import argparse
import os
import string
# input file = output_of_file_from_Task_1
# output_file = open('"alphabet"-words-new_darwin', 'w')


def get_each_alphabet(in_file, out_file, current_alpha):
    lines = in_file.readlines()
    for j in range(len(lines)):
        if lines[j][0] == current_alpha:
            out_file.write(lines[j])
    out_file.close()


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("input_file", help="Enter Input File Name")
    file = parse.parse_args()
    name, ext = os.path.splitext(file.input_file)
    alphabet = list(string.ascii_lowercase)
    for i in range(26):
        in_file = open(file.input_file)
        out_filename = alphabet[i]+'-words-' + name + ext
        out_file = open(out_filename, 'w')
        get_each_alphabet(in_file, out_file, alphabet[i])
        in_file.close()


if __name__ == '__main__':
    main()
