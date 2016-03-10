#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 7, 2016
 Program uses argparse to get input and output files (1.0 pt)
 Program uses any sort of dictionary to correctly count words in the text and returns the correct words and their counts for the 20 most common words (3 pts.)
@author: York
'''
import argparse
import collections


def parser_file_input():
    """Function takes a file as input and ask for a name for output file"""
    parser = argparse.ArgumentParser(
            description="""Input a file to use and an output file name"""
            )
    parser.add_argument(
                '--input',
                required=True,
                type=str,
                help='Enter the name of the file containing text.'
            )
    parser.add_argument('--output',required=True,type=str,help='Write into new file.')
    return parser.parse_args()


def cleanup(quote):
   
    cleaned_quote_0 = quote.lower()
    cleaned_quote_1 = cleaned_quote_0.replace(".", "").replace(",", "").replace(";","").replace("'","").replace(")","").replace("(","").replace(":","").replace("!","")
    cleaned_quote_2 = cleaned_quote_1.replace("\n\n", " ")
    return cleaned_quote_2


def makelist(parsed_quote):
    parsed = parsed_quote.split(" ")
    return parsed


def make_dict(quote_as_list):
    word_count = []
    for word in quote_as_list:
        total = 0
        for item in quote_as_list:
            if word == item:
                total += 1
        word_count.append(total)
    zip_dict = dict(zip(quote_as_list, word_count))
    return zip_dict


def top_twenty_words(the_dict):
    #top_ten = heapq.nlargest(10, the_dict, key=the_dict.get)
    top_twenty_sorted = sorted(the_dict.items(), key=lambda x: (-x[1], x[0]))[:20]
    return top_twenty_sorted


def write_file(word_count_dict,o):
    counted=collections.OrderedDict(word_count_dict)
    with open(o,'w') as the_output_file:
        for key,value in counted.items():
            the_output_file.write('{}\t{} \n'.format(key,value))
    return counted


def main():
    args = parser_file_input()
    with open(args.input, 'r') as thats_the_file:
        quote=thats_the_file.read()
        #print(quote)

    cleaned_quote = cleanup(quote)
    #print(cleaned_quote)
    quote_as_list = makelist(cleaned_quote)
    #print(quote_as_list)
    word_count_dict = make_dict(quote_as_list)
    #print(word_count_dict)
    top_twenty = top_twenty_words(word_count_dict)
    print("\n\nThe twenty most common words in the dictionary and their word counts:\n")
    for item in top_twenty:
        print('%s\t\t%s'%(item[0],item[1]))
        
        #print(item[0] + "\t" + str(item[1]))
    print("\n\n")
    o=args.output
    counted= write_file(word_count_dict,o)
    #print(counted)


if __name__ == '__main__':
    main()