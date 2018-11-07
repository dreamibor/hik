#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_char_dict = defaultdict(int)
    for char in a:
        a_char_dict[char] += 1
    counter = 0
    for char in b:
        if a_char_dict[char] != 0:
            a_char_dict[char] -= 1
        else:
            counter += 1
    for value in a_char_dict.values():
        counter += value
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
