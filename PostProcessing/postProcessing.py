# Program : To make the train set such that there are no OOV's.
# Language : python3
# Author : S.Moris

# Import necessary libraries
import os
import sys
import re
import numpy as np 
# Give the text file paths as an input.
directory = sys.argv[1] # Where the training data is present.
listDir = sys.argv[2] # Where the unique_word list is present.
devDir = sys.argv[3] # Where the 10% extracted lines are present.

for file in os.listdir(directory):
    if file != "dev.txt":
        lines = open(listDir + '/' + "unique_words_" + file + '.list','r').readlines()
        with open(directory + '/' + file,'a') as source:
            with open(devDir + + '/' + 'dev_' + file,'r') as dev:
                text = source.read()
                data = dev.readlines()
                for words in lines:
                    if ~re.search(words,text) :
                        for line in data:
                            if re.search(words,line):
                                source.write(line)


