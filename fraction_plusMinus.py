# Purpose: Given a list of integers, return the fraction of
# positive ints, negative ints, and zeros as decimal values,
# each printed on their own line and rounded to six decimal places.

from decimal import *

# Correct solution for HackerRank problem:
def plusMinus(arr):
    num_pos = 0
    num_neg = 0
    num_zero = 0
    arr_length = len(arr)
    for num in arr:
        if num > 0:
            num_pos += 1
        elif num < 0:
            num_neg += 1
        else:
            num_zero += 1
    frc_pos = (num_pos / arr_length)
    frc_neg = (num_neg / arr_length)
    frc_zero = (num_zero / arr_length)
    print(frc_pos)
    print(frc_neg)
    print(frc_zero)
    return frc_pos, frc_neg, frc_zero

# Alternative solution using Decimal class to clean-up output:
def plusMinus(arr):
    num_pos = 0
    num_neg = 0
    num_zero = 0
    arr_length = Decimal(len(arr))
    for num in arr:
        if num > 0:
            num_pos += 1
        elif num < 0:
            num_neg += 1
        else:
            num_zero += 1
    getcontext().prec = 6
    frc_pos = (num_pos / arr_length).quantize(Decimal('.000000'))
    frc_neg = (num_neg / arr_length).quantize(Decimal('.000000'))
    frc_zero = (num_zero / arr_length).quantize(Decimal('.000000'))
    print(frc_pos)
    print(frc_neg)
    print(frc_zero)
    return frc_pos, frc_neg, frc_zero

ex_list = [-4, 3, -9, 0, 4, 1]
plusMinus(ex_list)
