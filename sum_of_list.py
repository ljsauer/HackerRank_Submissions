# Purpose: Calculate the sum of the elements in a list of integers.


def aVeryBigSum(ar):
    big_sum = 0
    for num in ar:
        big_sum += num
    return big_sum

ar = [10000001, 10000004, 10000008, 10000010]
print(aVeryBigSum(ar))
