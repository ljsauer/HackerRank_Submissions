# Purpose: Given five positive integers, find the minimum and maximum values
# that can be calculated by summing only four of the five integers. Print the
# values on a single line separated by a space.

import math
import random

def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0
    arr.sort()
    min_sum = sum(arr[0:4])
    max_sum = sum(arr[1:5])
    return (min_sum, max_sum)

def Rand(start, end, num):
    rand_list = []
    for i in range(num):
        rand_list.append(random.randint(start, end))
    return rand_list

example = Rand(1, 1000, 5)
print(example)
print(miniMaxSum(example))
