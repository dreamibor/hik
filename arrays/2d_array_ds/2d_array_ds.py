#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    concat_arr = []
    max_sum = -100 # All negative numbers
    for num in arr:
        concat_arr += num
    for i in range(7,29):
        if (i+1)%6 != 0:
            hourglass_sum = concat_arr[i] + concat_arr[i-7] + concat_arr[i-6] + concat_arr[i-5] + concat_arr[i+5] + concat_arr[i+6] + concat_arr[i+7]
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
