#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sumArr = sum(arr)
    minNum = sumArr - arr[1]
    maxNum = sumArr - arr[1]
    for i in arr:
        x = sumArr - i
        if minNum >= x:
            minNum = x
        if maxNum <= x:
            maxNum = x
    print(str(minNum) + " " + str(maxNum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)