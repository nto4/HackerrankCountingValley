#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    alt = 0
    count = 0
    prealt = 0
    for i in range(n):
        if s[i] == 'U': #seviyeyi 1 artır 
            alt += 1
        elif s[i] == 'D':#seviyeyi 1 azalt
            alt -= 1
        if alt == 0 and prealt < 0: # eğer seviye şuanda 0 ise
        #ve 1 öceki adımda - de ise vadiden çıktık vadiyi 1 artır
            count += 1
        prealt = alt
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
