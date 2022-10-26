#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

def timeConversion(s):
    in_time = datetime.strptime(s, "%I:%M:%S%p")
    out_time = str(in_time)
    return out_time[11:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
