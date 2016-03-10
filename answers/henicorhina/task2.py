# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 11
Oscar Johnson 4 March 2016
"""

import argparse
import os


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
    counts how many words start with the letter "t"
    and writes these to a file
    """
    path = os.path.abspath(args.file_input)
    basename = os.path.basename(path) 
    base_t = "T-words-" + basename
    #print(base_t, type(base_t)) #debugger
    with open(args.file_input, 'r') as my_file:
        with open(base_t, 'w') as my_file2:
            for line in my_file:
                if line[0] == "t":
                    line.strip('\n')
                    my_file2.write(line)



def main():
    args = get_args()
    t_words(args)
    
if __name__ == '__main__':
    main()