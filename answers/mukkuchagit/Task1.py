#!/usr/bin/env python
# encoding: utf-8
"""
Files; assignment 11.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import operator
import argparse
import re
# text = open('c-darwin-chapter-1.txt')
# output_file = open('new_darwin.txt', 'w')


def blunt_word(text):
        read_file = text.read()
        read_file = re.sub(r'[^\w\s\n\n]', ' ', read_file)
        wordstring = read_file.replace("\n", "").replace("  ", " ").casefold()
        return wordstring


def word_list(wordstring):
    wordlist = wordstring.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(list(wordlist).count(w))
    return dict(zip(wordlist, wordfreq))


def sort_all(Ziplst):
    all_sorted = sorted(Ziplst.items(), key=operator.itemgetter(1), reverse=True)[:]
    return all_sorted


def output_function(in_file, out_file):
    wordstring = blunt_word(in_file)
    Ziplst = word_list(wordstring)
    sorted_words = sort_all(Ziplst)
    for i in range(20):
        print('{:15}{:4d}'.format(sorted_words[i][0], sorted_words[i][1]))
    for j in range(len(sorted_words)):
        out_file.write('{}\\t{}\\n\n'.format(sorted_words[j][0], sorted_words[j][1]))
    out_file.close()
    in_file.close()


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("input_file", help="Enter Input File Name")
    parse.add_argument("output_file", help="Enter Output File Name")
    files = parse.parse_args()
    in_file = open(files.input_file)
    out_file = open(files.output_file, 'w')
    output_function(in_file, out_file)


if __name__ == '__main__':
    main()
