# Purpose: Given a square matrix, return the absolute
# difference of the sums of its diagonals.


def diagonalDifference(arr):
    diag_one = 0
    diag_two = 0
    j = len(arr) - 1
    for i in range(len(arr)):
        diag_one += arr[i][i]
        diag_two += arr[i][j]
        j -= 1
    abs_diff = abs(diag_one - diag_two)
    return abs_diff

matrix = [[1, 4, 7],
          [2, 9, 9],
          [4, 6, 8]]

print(diagonalDifference(matrix))
