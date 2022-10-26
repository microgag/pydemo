#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Get lenght of the array
    length = len(arr);
    
    positiveCount = 0;
    negativeCount = 0;
    zeroCount = 0;
 
    output = []
    # Traverse the array and count the total number of
    # positive, negative, and zero elements.
    if length > 0 and length <= 100:
        for i in range(length):
            if (arr[i] > 0):
                positiveCount += 1;
            elif(arr[i] < 0):
                negativeCount += 1;
            elif(arr[i] == 0):
                zeroCount += 1;
            
        # Print the ratio of positive,
        # negative, and zero elements
        # in the array up to four decimal places.
        print("{0:.6f}".format((positiveCount / length)));
        print("%1.6f"%(negativeCount / length));
        print("%1.6f"%(zeroCount / length));

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
