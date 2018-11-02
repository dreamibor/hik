#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # 如果存在子字符串相同的话，必然存在字符相同，不需要使用字典。
    # result = "NO"
    # for index in range(len(s2)):
    #     if result == "NO":
    #         for index2 in range(index+1, len(s2)+1):
    #             if s2[index:index2] in s1:
    #                 result = "YES"
    #                 break
    #     else:
    #         break
    # return result
    result = "NO"
    for i in set(s2):
        if i in set(s1):
            result = "YES"
            break
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
