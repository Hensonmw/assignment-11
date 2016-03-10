# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 11
Oscar Johnson 4 March 2016
"""

import argparse
import os
import string


def get_args():
    parser = argparse.ArgumentParser(
            description="""takes input file from task 1""")
    parser.add_argument('--file',
                        dest = "file_input",
                        required = True,
                        help = "enter a .txt input file containing counts of words"
                        )
    return parser.parse_args()


def t_words(args):
    """
    counts how many words start with each letter of the alphabet
    and writes these to a file, each with the name of that letter
    """
    path = os.path.abspath(args.file_input)
    basename = os.path.basename(path) 
    for letter in string.ascii_uppercase:
        base = letter + "-words-" + basename
        with open(base, 'w') as my_file2:
            with open(args.file_input, 'r') as my_file:
                for line in my_file:
                    if line[0] == letter.lower():
                        line.strip('\n')
                        my_file2.write(line)
                    else:
                        pass



def main():
    args = get_args()
    t_words(args)
    
if __name__ == '__main__':
    main()