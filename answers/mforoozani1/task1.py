#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task1 to Write a program to count word usage in the text
count the most 20 common words use collection module, and argparser
"""
from collections import Counter
import argparse


def get_parser():
    """
   using argparse to takes the list  as input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputfile", required=True)
    parser.add_argument("--outputfile", required=True)
    args = parser.parse_args()
    return args


def lowercase_replace(string):
    """
    remove, and change all characters to lower case, count the frequency
    words
    """

    text1 = string.replace(",", " ").replace(".", " ")
    text2 = text1.replace("?", " ").replace("/", " ").replace("!", " ")
    text3 = text2.replace(":", " ").replace(";", " ").casefold()
    text4 = text3.replace(")", " ").replace(" (", " ")
    text5 = text4.replace("  ", " ")
    text6 = text5.split()
    # mylist.extend(text6)
    # return mylist
    return text6


def count_text(l):
        counttext = Counter(l)
        return counttext


def most_common(s):
    """
    find top most common and sort them in column
    """
    mostcommon = s.most_common(20)
    for i in mostcommon:
        A = "{}{}{}".format(i[0], "\t", i[1])
        print(A)


def tab_delimited_file(d, outputfile):
    """
    sort and formatted all the words in tab-delimited format and write them in
    output file
    """
    sorted_dict = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    for i in sorted_dict:
        if len(i[0]) < 8:
            outputfile.write("{0}\t{1}\n".format(i[0], i[1]))
        if len(i[0]) >= 8 and len(i[0]) < 16:
            outputfile.write("{0}\t{1}\n".format(i[0], i[1]))
        if len(i[0]) >= 16:
            outputfile.write("{0}\t{1}\n".format(i[0], i[1]))


def main():
    args = get_parser()
    with open(args.inputfile, "r") as inputfile:
        inputfile_string = inputfile.read()
    outputfile = open(args.outputfile, "w")
    A = lowercase_replace(inputfile_string)
    B = count_text(A)
    most_common(B)
    tab_delimited_file(B, outputfile)


if __name__ == '__main__':
    main()
