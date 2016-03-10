#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 7, 2016
Program uses argparse to get the input filename (1.0 pt)
Program correctly writes the requested file containing words that start with "T" and the count of these words (3 pts.)
@author: York
'''
import argparse
import os
from string import ascii_lowercase


def get_parser():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    
    args = parser.parse_args()
    return args


def count_t_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 't':
                    A.append(i)
                  
                m = os.path.join("t-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)


def main():
    args = get_parser()
    inputfile = args.input
  
    count_t_words(inputfile)


if __name__ == '__main__':
    main()