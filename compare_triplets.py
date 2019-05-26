# Purpose: Compare lists a and b at their corresponding
# indices. If a[0] > b[0], list a gains 1 point, and so on.
# Return new list with each list's totaled points ([a, b]).


def compareTriplets(a, b):
    a_points = 0
    b_points = 0
    for i in range(3):
        if a[i] > b[i]:
            a_points += 1
        elif b[i] > a[i]:
            b_points += 1
    return a_points, b_points

# Alternatively, and more Pythonically, use the zip function:
def compareTriplets(a, b):
    a_points = 0
    b_points = 0
    for num_a, num_b in zip(a, b):
        if num_a > num_b:
            a_points += 1
        elif num_b > num_a:
            b_points += 1
    return [a_points, b_points]

a = [1, 2, 4]
b = [3, 1, 4]
point_list = compareTriplets(a, b)
print(point_list)
print(type(point_list))     # Ensures correct output type
