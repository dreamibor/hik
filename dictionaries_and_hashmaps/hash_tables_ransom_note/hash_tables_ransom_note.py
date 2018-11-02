#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    output = "Yes"
    magazine_dict = defaultdict(int)
    for word in magazine:
        magazine_dict[word] += 1
    for word in note:
        if magazine_dict[word] != 0:
            magazine_dict[word] -= 1
        else:
            output = "No"
            break
    print(output)
            

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
