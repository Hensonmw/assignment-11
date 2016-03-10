#!/usr/bin/env python
# utf-8

"""
Program counts words usage in the darwin-chapter1 in decreasing order for top20
most common words.
Created by Pramod Pantha on 6 March, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


import argparse
import collections


def parser():
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", required=True,
                        help="Enter '--input_file', space, and then" +
                        " the name of the input file.", type=str)
    parser.add_argument("--output_file", required=True,
                        help="Enter '--input_file', space, and then" +
                        " the name of the output file.", type=str)
    args = parser.parse_args()
    return args


def edited_word_list(raw_text):
    line_list = []
    punctuation = set("(),.?/!;:'\n\t")
    for line in raw_text:
        if line != "\n":
            cleaned_line_0 = "".join(c for c in line if c not in punctuation)
            cleaned_line_1 = cleaned_line_0.casefold()
            parsed = cleaned_line_1.split(" ")
            line_list.extend(parsed)
    return line_list


def word_count_dictionate(list_of_lines):
    # gives dictionary of all word count
    counterdict = collections.Counter(list_of_lines)
    return counterdict


def top_words(the_dict):
    # gives top 20 most frequent words
    top20 = the_dict.most_common(20)
    return top20


def file_writer(word_count_dict, output_file):
    sorted_dict = sorted(word_count_dict.items(), key=lambda x: (-x[1], x[0]))
    # print("sorted_dict: ", sorted_dict)
    for item in sorted_dict:
        if len(item[0]) < 8:
            # print(len(item))
            output_file.write("{}{}{}{}".format(item[0], "\t", item[1], "\n"))
        if len(item[0]) >= 8 and len(item[0]) < 16:
            output_file.write("{}{}{}{}".format(item[0], "\t", item[1], "\n"))
        if len(item[0]) >= 16:
            output_file.write("{}{}{}{}".format(item[0], "\t", item[1], "\n"))


def main():
    args = parser()
    input_file = open(args.input_file, "r")
    output_file = open(args.output_file, "w")
    word_list = edited_word_list(input_file)
    # print(word_list)
    word_count_dict = word_count_dictionate(word_list)
    # print(word_count_dictionate)
    top_twenty = top_words(word_count_dict)
    number = 20
    print("\n\nThe {} most common words in the dictionary and".format(number) +
          " their counts:\n")
    # gives top twenty words printing them in good format
    for item in top_twenty:
        if len(item[0]) < 8:
            # print(len(item))
            print("{}{}{}".format(item[0], "\t", item[1]))
        if len(item[0]) >= 8:
            print("{}{}{}".format(item[0], "\t", item[1]))
    print("{}".format("\n\n"))
    file_writer(word_count_dict, output_file)
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
