#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 7, 2016
 Program uses argparse to get the input filename (1.0 pt)
 Program correctly writes the requested files, names according to letters of the alphabet, where each file contains words that start with the corresponding alphabet letter, and the count of these words (3 pts.)
@author: York
'''
from pstats import count_calls
'''
Created on Mar 7, 2016

@author: York
'''
import argparse
import os
from string import ascii_lowercase


def get_parser():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    
    args = parser.parse_args()
    return args


def count_a_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'a':
                    A.append(i)
                    #print(A)
    m = os.path.join("a-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)
            
            
def count_b_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'b':
                    A.append(i)
                    #print(A)
    m = os.path.join("b-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)
            
            
def count_c_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'c':
                    A.append(i)
                    #print(A)
    m = os.path.join("c-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)       
        
        
def count_d_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'd':
                    A.append(i)
                    #print(A)
    m = os.path.join("d-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)


def count_e_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'e':
                    A.append(i)
                    #print(A)
    m = os.path.join("e-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)


def count_f_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'f':
                    A.append(i)
                    #print(A)
    m = os.path.join("f-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)


def count_g_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'g':
                    A.append(i)
                    #print(A)
    m = os.path.join("g-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)


def count_h_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'h':
                    A.append(i)
                    #print(A)
    m = os.path.join("h-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)
            
            
def count_i_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'i':
                    A.append(i)
                    #print(A)
    m = os.path.join("i-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)
            
            
def count_j_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'j':
                    A.append(i)
                    #print(A)
    m = os.path.join("J-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)
                        
            
def count_k_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'k':
                    A.append(i)
                    #print(A)
    m = os.path.join("k-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)
            
                      
def count_l_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'l':
                    A.append(i)
                    #print(A)
    m = os.path.join("l-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)
            
                        
def count_m_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'm':
                    A.append(i)
                    #print(A)
    m = os.path.join("m-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)
            
                        
def count_n_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'n':
                    A.append(i)
                    #print(A)
    m = os.path.join("n-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)
            
                       
def count_o_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'o':
                    A.append(i)
                    #print(A)
    m = os.path.join("o-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)
            
            
def count_p_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'p':
                    A.append(i)
                    #print(A)
    m = os.path.join("p-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)
            
                      
def count_q_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'q':
                    A.append(i)
                    #print(A)
    m = os.path.join("q-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)                        


def count_r_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'r':
                    A.append(i)
                    #print(A)
    m = os.path.join("r-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)    
            
            
def count_s_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 's':
                    A.append(i)
                    #print(A)
    m = os.path.join("s-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)    
                       
            
def count_t_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 't':
                    A.append(i)
                    #print(A)
    m = os.path.join("t-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)             
            
            
def count_u_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'u':
                    A.append(i)
                    #print(A)
    m = os.path.join("u-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)    
            
            
def count_v_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'v':
                    A.append(i)
                    #print(A)
    m = os.path.join("v-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)    
                 
            
def count_w_words(inputfile):
    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'w':
                    A.append(i)
                    #print(A)
    m = os.path.join("w-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)    
                      
            
def count_x_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'x':
                    A.append(i)
                    #print(A)
    m = os.path.join("x-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)    
            
                      
def count_y_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'y':
                    A.append(i)
                    #print(A)
    m = os.path.join("y-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)    
            
                 
def count_z_words(inputfile):

    for letter in ascii_lowercase:
        A = []
        with open(inputfile, 'r') as d:
            for i in d:
                if i[0] == 'z':
                    A.append(i)
                    #print(A)
    m = os.path.join("z-words-" + inputfile)
    with open(m, 'w') as outputfile:
        for i in A:
            outputfile.write(i)    


def main():
    args = get_parser()
    inputfile = args.input
    count_a_words(inputfile)
    count_b_words(inputfile)
    count_c_words(inputfile)
    count_d_words(inputfile)    
    count_e_words(inputfile)
    count_f_words(inputfile)
    count_g_words(inputfile)
    count_h_words(inputfile)
    count_i_words(inputfile)
    count_j_words(inputfile)
    count_k_words(inputfile)
    count_l_words(inputfile)
    count_m_words(inputfile)
    count_n_words(inputfile)
    count_o_words(inputfile)
    count_p_words(inputfile)
    count_q_words(inputfile)
    count_r_words(inputfile)
    count_s_words(inputfile)
    count_t_words(inputfile)
    count_u_words(inputfile)
    count_v_words(inputfile)
    count_w_words(inputfile)
    count_x_words(inputfile)
    count_y_words(inputfile)
    count_z_words(inputfile)
    

if __name__ == '__main__':
    main()