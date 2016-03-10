# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 07:45:36 2016

@author: Marco
"""

"""
In the file c-darwin-chapter-1.txt is Chapter 1 from Darwin's Origin of 
Species. Similar to your previous assignment, write a program to count word 
usage in the text within this file (you are free to use most/all of that 
previous code). Have this program print out, in decreasing order (most common 
to least common) the 20 most common words and the count of each word used. 
Your program should contain a main loop and an ifmain statement, it should be 
formatted correctly, and you should use argparse to get the name of the input 
and output files from the user. You may use any type of dictionary object in 
your code. You should print your Top 20 results to the screen using the 
.format() string method, and your results should be prettily spaced (again, 
using .format()) so that the column of words and word counts are justified 
left, like so:

the         100
a           80
and         70
during      50

You should also write your results for ALL words to a file, formatted in 
tab-delimited format (again, use the .format() method). Tab-delimited data 
look like:

word\tcount\n
the\t100\n
a\t80\n
and\t70\n
during\t50\n
"""
# Import Modules
import re
import collections
import argparse


def parser_function():
    '''
    Function to parse arguments
    '''
    parser = argparse.ArgumentParser(description="""my argument parser""")
    # Adding an argument to 'parse'    
    parser.add_argument('in_file', type=str, 
                        help='after placing your file and script in the same '
                        'folder, type the name of your file after the name '
                        'of this script in the terminal.')
    parser.add_argument('out_file',type=str, help='place the output file name '
                        'after the input file name')
    args = parser.parse_args()
    inp = args.in_file
    out = args.out_file
    return inp, out


def file_opener(my_file):
    '''
    Opens file transorming lines into list elements and to string afterwards.
    '''
    my_list = []    
    with open(my_file,'r') as darwin:
        for line in darwin:
            my_list.append(line)
    string = "".join(my_list)
    return string


def string_standizer(my_string):
    '''
    this function takes all kinds of pontuation out of our string, including
    the apostrophe (') of words like can't, for example. The output will
    comprehend a lower case string with words separated by spaces.
    '''
    low = my_string.casefold()
    new_lines_out = re.sub("\n"," ",low)
    without_apos = re.sub("'","",new_lines_out)
    without_pontuation = re.sub("\W"," ",without_apos)
    one_space = re.sub("\s+"," ",without_pontuation)
    end_stripper = one_space.strip()
    return end_stripper


def counter_function(my_string):
    '''
    The input is a string. 
    this function uses the Counter function from the collections' module to
    count the values in a list and return a dictionary with the number of
    occurrencies for each word
    '''
    string_list = string_standizer(my_string)
    listagem = string_list.split(" ")
    count = collections.Counter(listagem)
    return count


def main():
    inp, output = parser_function()
    my_string = file_opener(inp)
    std_string = string_standizer(my_string)
    count = counter_function(std_string)
    more_freq = count.most_common(20)
    for word,freq in more_freq:
        print('{0}\t{1}'.format(word, freq))
    with open(output,'w') as out:
        for key, val in count.items():
            out.write('{:17}\t{:>3}\n'.format(key,val))


if __name__ == '__main__':
    main()