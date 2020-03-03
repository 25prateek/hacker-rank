#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    p = 0

    while(p < len(c) - 2):
        if c[p + 2] != 1:
            p +=2
            jumps += 1
        else:
            p +=1
            jumps += 1
    if p == len(c) - 2:
        jumps += 1
    
    return jumps
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

