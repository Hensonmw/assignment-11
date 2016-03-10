#! /usr/bin/env python
# encoding UTF-8

'''
Assignment11Task3 biol7800
ZacCarver 03/08/2016
'''


import argparse
from string import ascii_lowercase
import os


def args():
    parser = argparse.ArgumentParser(description='''task1 product file in''')
    parser.add_argument('--infile', type=str, help='enter file')
    return parser.parse_args()


def darsalpha(a):
    for letter in ascii_lowercase:
        darsalphalist = []
        for word in a:
            if word[0] == letter:
                darsalphalist.append(word)
        fwrite = os.path.join(str.upper(letter) + '-words-' + a)
        with open(fwrite, 'w') as t:
            for i in darsalpha:
                t.write(i)


def main():
    arg = args()
    a = open(arg.infile, 'r')
    darsalpha(a)

if __name__ == '__main__':
    main()
