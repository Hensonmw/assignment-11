#! /usr/bin/env python
# encoding UTF-8

'''
Assignment11Task1 biol7800
ZacCarver 03/08/2016
'''


import argparse
from collections import Counter
import re


def args():
    parser = argparse.ArgumentParser(description='''20 most common words\
    from input file''')
    parser.add_argument('--infile', type=str, required=True, help='enter file')
    parser.add_argument('--outfile', type=str, required=True, help='writes \
    product to file')
    return parser.parse_args()


def dars_w(f):
    s = f.read().lower()
    word_dict = []
    words = re.split("\W+", s)
        #making the counted dictionary
    for i in words:
        words += 1
    return word_dict

'''
def count_w(w):
    counted = Counter(w)
    return counted
'''


def pretty_dars(words):
    freq = Counter(words).most_common(20)
    return freq


def write_dars(words, o):
    counted = Counter(words)
    with open(o, 'w') as fileout:
        for key, value in counted.items():
            fileout.write('{}\t{}\n'.format(key, value))
    return counted


def main():
    arg = args()
    f = open(arg.infile, 'r')
    o = arg.outfile
    #s = dars_str(i)
    words = dars_w(f)
    write_dars(words, o)
    freq = pretty_dars(words)
    for key, value in freq:
        print('{}\t{}'.format(key, value))

if __name__ == '__main__':
    main()
