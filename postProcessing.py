# Program : To make the train set such that there are no OOV's.
# Language : python3
# Author : S.Moris

# Import necessary libraries
import os
import sys
import numpy as np 
# Give the text file paths as an input.
directory = sys.argv[1] # Where the training data is present.
listDir = sys.argv[2] # Where the unique_word list is present.
devDir = sys.argv[3] # Where the 10% extracted lines are present.

for file in os.listdir(directory):
    if file != "dev.txt":
        None












