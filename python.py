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


# def plusMinus(arr):
#     # Write your code here
#     length = len(arr)
#     pos = len([i for i in arr if i > 0])
#     zer = len([i for i in arr if i == 0])
#     neg = len([i for i in arr if i < 0])
#     print("{:.6f}".format(pos/length))
#     print("{:.6f}".format(neg/length))
#     print("{:.6f}".format(zer/length))


# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)


def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    print(sum(arr[:4]), sum(arr[1:]))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
