#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:55:17 2016

@author: Glaucia
"""
import collections
import re
import argparse

def openningfile(filename):
    """opens a text file whose name is given as input in the shell. Returns a string that will be used
    in word counts"""
    storingfile=[]
    with open(filename,'r') as my_file:
        for line in my_file:
            storingfile.append(line)  
        text ="".join(storingfile)
    return text


def dealing (wordsfile):
    """edits a string removing ponctuation, spaces new lines, and capital letters
    to allow adequate word count. Returns the edited string"""
    wordsfile=re.sub("'","",wordsfile)
    wordsfile=re.sub('"',"",wordsfile)
    wordsfile=re.sub("\n","",wordsfile)
    wordsfile=re.sub("\W"," ",wordsfile)
    wordsfile=re.sub("\s+"," ",wordsfile)
    wordsfile=wordsfile.lower()
    wordsfile=wordsfile.strip()
    return wordsfile
    

def Writingdictionary(wordsfile,filename):
    """counts the words in the string provided in the last two functions, writes a file 
    with all the word counts (tab delimited). The argument filename takes the name of the file
    that will be writen. Returns a dictionary with all the words counts"""
    wordlist = wordsfile.split(" ")
    counterdict=collections.Counter(wordlist)
    with open (filename,'w') as my_file:
        for key,value in counterdict.items():
            my_file.write("{0}\t{1}\n".format(key,value))
    return counterdict


def Counting(counterdict):
    """gets the 20 most common words and prints them nicelly justified usinf .format"""
    top20=counterdict.most_common(20)
    listoflists=(sorted(top20, key=lambda top20: top20[1],reverse=True))
    for lis in listoflists:
        line_new = "{0:<20} {1:1d}".format(lis[0],lis[1])
        print(line_new) 

def arguments():
    """parsing arguments to allow changing input file and output name"""
    parser = argparse.ArgumentParser(description="""my argument parser""")   
    parser.add_argument('input', type=str, help='give the name of your input file')
    parser.add_argument('output', type=str, help='give a name for your output file')
    args = parser.parse_args()
    return args
    
    
def main():
    arg=arguments()
    inpu=arg.input
    outp=arg.output
    chapter=openningfile(inpu)
    wordsfile=dealing(chapter)
    counterdict=Writingdictionary(wordsfile,outp)
    Counting(counterdict)
    
    
if __name__ == '__main__':
    main()      
    