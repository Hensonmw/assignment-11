#!/usr/bin/env python
# encoding: utf-8
"""
Files; assignment 11.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import argparse
import os
# input_file = open('new_darwin.txt')
# output_file = open('Only-T-words-new_darwin', 'w')


def get_T_words(in_file, out_file):
    lines = in_file.readlines()
    for j in range(len(lines)):
        if lines[j][0] == 't':
            out_file.write(lines[j])
    out_file.close()
    in_file.close()


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("input_file", help="Enter Input File Name")
    file = parse.parse_args()
    name, ext = os.path.splitext(file.input_file)
    output_filename = 'Only-T-words-' + name + ext
    in_file = open(file.input_file)
    out_file = open(output_filename, 'w')
    get_T_words(in_file, out_file)


if __name__ == '__main__':
    main()
