#!/bin/python3

import math
import os
import random
import re
import sys

def lonelyinteger(a):
    result = [val for val in a if a.count(val) == 1]
    for i in result:
        return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
