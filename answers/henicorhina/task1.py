# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 11
Oscar Johnson 4 March 2016
"""

import re
import collections
import argparse
import os


def get_args():
    parser = argparse.ArgumentParser(
            description="""takes input file and provides count of the 10 most 
            common words""")
    parser.add_argument('--file',
                        dest = "file_input",
                        required = True,
                        help = "enter a .txt input file containing strings of text"
                        )
    parser.add_argument('--file_output',
                        dest = "file_output",
                        required = True,
                        help = "enter a .txt output file to take your results"
                        )
    return parser.parse_args()


def quote_dict(args):
    """
    function takes text as a file and creates a dictionary of words
    then returns a count all words as a list of tuples
    """
    #new counter
    count_all = collections.Counter()
    with open(args.file_input) as my_text:
        for line in my_text:
            text = line.lower() #lowercase all text
            text = re.sub("['-;:()&?!%,]", '', text) #remove non-alphanumeric chars
            text = re.sub("[\n]", '', text) #remove newlines
            text = re.sub('[.]', ' ', text) #replace periods with whitespace
            l = text.split() #listify
            # count of all words
            for word in l:
                count_all[word] += 1
    return count_all


def word_printer(args, d):
    """
    takes a dictionary of word counts and prints all to a file
    in format: word\tcount\n
    """
    my_dict = dict(d) # convert to regular dictionary
    count_of_words = [] 
    for key, value in my_dict.items():
        # add words and values to list in form of tuples
        count_of_words.append((value, key))
    count_of_words.sort(reverse=True) #sort words in descending abundance
    #print(count_of_words) # print debugger
    with open(args.file_output, 'w') as my_file2:
        #for line in my_file2:
        for value, key in count_of_words:
            x = "{}\t{}\n".format(key, value)
            my_file2.write(x)
    print(os.path.abspath(args.file_output))



def main():
    args = get_args()
    count = quote_dict(args)
    print("here are the twenty most common words ")
    for key, value in count.most_common(20):
        print('{:10} {:10}'.format(key, value))
    word_printer(args, count)

if __name__ == '__main__':
    main()