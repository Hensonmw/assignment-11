#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 11, Task 1
Austen T. Webber
2016_3_7
"""


from collections import Counter
import argparse
import re


def fileimporter():
    parser = argparse.ArgumentParser(
        description="Get input and output files from user")
    parser.add_argument(
        "--input",
        required=True,
        help="Input file:",
        type=str
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output file:",
        type=str
    )
    return parser.parse_args()


def text_count(string):
    with open(string, "r") as string:
        string = string.read()
        list = re.split('\W+', string)
        my_dict = [str.lower(word) for word in list]
    return my_dict


def final_count(text):
    counting = Counter(text).most_common(20)
    return counting


def output(all_count, outputfile):
    with open(outputfile, 'w') as outputfile:
        text_count = Counter(all_count)
        for word, count in all_count.items():
            outputfile.write('{0}\t{1}\n'.format(word, count))


def main():
    textinput = fileimporter()
    all_count = text_count(textinput.input)
    end_counts = final_count(all_count)
    print("Top 20 words in text file:")
    for item in end_counts:
        print("{0:<12}  {1:<12}".format(item[0], item[1]))
    output(all_count, textinput.output)


if __name__ == '__main__':
    main()
