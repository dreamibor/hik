#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    bracket_map = {"]":"[", "}":"{", ")":"("}
    stack = []
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        else:
            if not stack or bracket_map[char] != stack.pop():
                return "NO"
    return "NO" if stack else "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
