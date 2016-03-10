#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:04:18 2016

@author: Glaucia
"""
import os
import argparse

def oppenningfile(filename):
    """loops through alphabet letters, builds lists with words starting with different alphabet letters
    saves each list as tab delimited files in the format A-words-input name, B-words-input name, etc"""
    alphabet="abcdefghijklmnopqrstuvxwyz"
    for letter in alphabet:
        listbyletter=[]
        with open(filename,'r') as my_file:
            for line in my_file:
                if line[0] == letter:
                    listbyletter.append(line)
        writefilename=os.path.join(letter+"-words-"+filename)
        with open(writefilename,'w') as letterfile:
            for value in listbyletter:
                letterfile.write(value)
                    
                    
def arguments():
    """parsing arguments to allow changing input file"""
    parser = argparse.ArgumentParser(description="my argument parser")   
    parser.add_argument('input', type=str, help='give the name of your input file')
    args = parser.parse_args()
    return args

        
def main():
    arg=arguments()
    inpu=arg.input
    oppenningfile(inpu)

    
if __name__ == '__main__':
    main()      
