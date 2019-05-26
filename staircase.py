# Purpose: Prints a right-aligned staircase of '#'s
# of height 'n'.

def staircase(n):
    step = '#'
    stair_height = n
    while stair_height > 0:
        print(step.rjust(n, ' '))
        stair_height -= 1
        step += '#'

staircase(6)
