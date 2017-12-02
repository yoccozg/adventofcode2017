#!/usr/bin/env python3

def solve():
    '''For example, given the following spreadsheet:
    5 1 9 5
    7 5 3
    2 4 6 8
    The first row's largest and smallest values are 9 and 1, and their difference is 8.
    The second row's largest and smallest values are 7 and 3, and their difference is 4.
    The third row's difference is 6.

    In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.'''
    checksum = 0
    with open('input.txt') as f:
        for line in f:
            array = [int(x) for x in line.split('\t')]
            checksum = checksum + abs(max(array) - min(array))
    return checksum


print("result =", solve())
