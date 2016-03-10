# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:09:04 2016

@author: Marco
"""
"""
Task 2

Write a program that uses argparse to get the name of the tab-delimited file 
you created above from the user. Read that file into your program, and 
determine count of all words that start with the letter "t" (or "T"). Using 
the os.path module, write these t-starting words to a new tab-delimited file 
that has the same name as the input file, but with "T-words" prepended to the 
input filename. For example, if the input filename is "all-word-counts.txt", 
then your output file of t-words should be "T-words-all-word-counts.txt". You 
can accomplish these filename manipulations using the os.path module. Your 
program should contain a main loop and an ifmain statement, and it should be 
formatted correctly.
"""
# Import Modules
import re
import argparse
import os.path


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


def file_opener():
    '''
    Opens file transorming lines into list elements
    I adapted this function to read my output files, especifically.
    '''
    inp, out = parser_function()
    my_list = []   
    with open(inp,'r') as darwin:
        for line in darwin:
            item = re.sub("\s+"," ",line)
            my_list.append(item.strip())
    return my_list


def list_packer(my_list):
    '''
    Creates a list where each element comprhends a list with two items: word 
    and word count.
    '''
    list_of_lists = []
    for item in my_list:
        string_split = item.split(" ")
        list_of_lists.append(string_split)
    return list_of_lists
    

def get_words_by_letter(my_list,letter):
    '''
    Retrieve a list of words, and their counts, that starts with any desired 
    letter. The output resembles the one from the function list_packer.
    '''
    desired_words=[]
    for word in my_list:
        if word[0][0]==letter:
            desired_words.append(word)
        else:
            pass
    return desired_words


def list2file_writer(my_list):
    '''
    Saving lists to a txt file using os.path module
    '''
    inp, my_file = parser_function()
    path = os.path.dirname(inp)
    with open(os.path.join(path,my_file+"-"+inp),'w') as my_file:
        for word, count in my_list:
            my_file.write('{:17}\t{:>3}\n'.format(word,count))
            

def main():
    test = file_opener()
    list_of_lists = list_packer(test)
    get_t_words = get_words_by_letter(list_of_lists,'t')
    list2file_writer(get_t_words)


if __name__ == '__main__':
    main()
