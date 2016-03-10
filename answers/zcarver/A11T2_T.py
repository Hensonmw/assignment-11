#! /usr/bin/env python
# encoding UTF-8

'''
Assignment11Task2 biol7800
ZacCarver 03/08/2016
'''


import argparse
from string import ascii_lowercase
import os


def args():
    parser = argparse.ArgumentParser(description='''task1 product file in''')
    parser.add_argument('--infile', type=str, help='enter file')
    return parser.parse_args()


def t_addition(f):
    for letter in ascii_lowercase:
        darst = []
        with open(f, 'r') as f:
            for line in f:
                if line[0] == 't':
                    darst.append(line)
                    fwrite = os.path.join('t-words-' + f)
                    with open(fwrite, 'w') as t:
                        for i in darst:
                            t.write(i)


def main():
    f = args()
    t_addition(f.infile)

if __name__ == '__main__':
    main()
