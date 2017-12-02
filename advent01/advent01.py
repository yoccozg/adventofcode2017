#!/usr/bin/env python3

def solve(captcha):
    ''' For example:
    1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
    1111 produces 4 because each digit (all 1) matches the next.
    1234 produces 0 because no digit matches the next.
    91212129 produces 9 because the only digit that matches the next one is the last digit, 9.'''
    return sum([int(v) for idx, v in enumerate(captcha) if v == captcha[(idx + 1) % len(captcha)]])


with open('input.txt') as f:
    print("result =", solve(f.readline()))
