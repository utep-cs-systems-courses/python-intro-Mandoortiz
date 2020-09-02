#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:36:23 2020

@author: zitroaaa
"""
import re
import sys

def input_file_name():
    user_file = input("Enter name of input file: ")
    return user_file

def read_file(input_file):
    file = open(input_file,"r")
    contents = file.read()
    file.close
    return contents

def write_file(word_list):
    out = open("myoutput.txt","w")
    for words in word_list:
        out.write('%s\n' % words)
    out.close()
    
output_file = {}
user_file = input_file_name()
contents = read_file(user_file)
output_file = re.split(r'\W+',contents)
while('' in output_file):
    output_file.remove('')
    
output_file.sort()
print(output_file)
write_file(output_file)
