#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    n = len(a)
    # Relationship: a[n-d+i] = a[i]

    # Using another new array:
    # new_a = [0] * n
    # for i in range(n):
    #     new_a[(n-d+i)%n] = a[i]
    # return new_a

    # In the same array:
    # A dictionary to store temp values.
    temp = {}
    for i in range(n):
        if i in temp.keys():
            temp[(n-d+i)%n] = a[(n-d+i)%n]
            a[(n-d+i)%n] = temp[i]
            del temp[i] # It's okay to don't delete used temp value since corresponding index will only appear once.
        else:
            temp[(n-d+i)%n] = a[(n-d+i)%n]
            a[(n-d+i)%n] = a[i]
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
