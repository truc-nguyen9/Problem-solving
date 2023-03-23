#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    numPos = 0
    numNeg = 0
    numZero=0
    totalNum = len(arr)
    for i in arr:
        if i < 0:
            numNeg+=1
        elif i > 0:
            numPos+=1
        else:
            numZero+=1;
    x = round(numPos/totalNum, 6)
    y = round(numNeg/totalNum,6)
    z = round(numZero/totalNum,6)
    print(x)
    print(y)
    print(z)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
