#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:42:30 2016

@author: Glaucia
"""

import os
import argparse

def oppenningfile(filename):
    """opens file with all the words counts and loops through file lines to find
    matchings with the the "t" letter as the starting letter of the line. Grabs all the
    words starting in t puts in a list and writes the list in a tab delimited file named "T-words plus the
    given input"""
    list1=[]
    with open(filename,'r') as my_file:
        for line in my_file:
            if line[0] == "t":    
                list1.append(line)
    writefilename=os.path.join("T-words-" + filename)
    with open(writefilename,'w') as tfile:
        for value in list1:
            tfile.write(value)            
                
   
def arguments():
    """parsing arguments to allow changing input file"""
    parser = argparse.ArgumentParser(description="my argument parser")   
    parser.add_argument('input', type=str, help='give the name of your input file')
    args = parser.parse_args()
    return args

    
    
def main():
    arg=arguments()
    inpu=arg.input
    chapter=oppenningfile(inpu)
    print(chapter)
    
    
if __name__ == '__main__':
    main()      
