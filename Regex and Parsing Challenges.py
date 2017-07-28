''' Python question by HackerRank
TODO 1: "Introduction to Regex Module"
You are given a string N.
Your task is to verify that N is a floating point number.
In this task, a valid float number must satisfy all of the following requirements:
 Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
 -+4.5
 Number must contain at least 1 decimal value.
For example:
✖
 12.
✔
12.0
 Number must have exactly one . symbol.
 Number must not give any exceptions when converted using float(N).
Input Format:
The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.
Constraints: 0 < T < 10
Output Format: Output True or False for each test case.

'''

from fractions import Fraction
from functools import reduce
import re
import sys


# TODO 1: "Introduction to Regex Module"
def string_from_dot(input_line):
    if input_line.isdigit():
        # print(input_line, end=' is ')
        print('True')
        return 0
    else:
        # print(input_line, end=' is ')
        print('False')
        return 0


def check_number(input_line):
    if input_line[0] == '+' or input_line[0] == '-':
        input_line = input_line[1:]
    if input_line[0] == '.':
        string_from_dot(input_line[1:])
        return 0
    else:
        input_list = input_line.split('.')
        if len(input_list) != 2:
            # print(input_line, end=' is ')
            print('False')
            return 0
        else:
            if input_list[0].isdigit() and input_list[1].isdigit():
                # print(input_line, end=' is ')
                print('True')
                return 0
            else:
                # print(input_line, end=' is ')
                print('False')
                return 0


def introduction_to_regex():
    number_of_tests = int(input().lstrip().rstrip())
    for _ in range(int(number_of_tests)):
        input_line = input().lstrip().rstrip()
        check_number(input_line)


def main():
    introduction_to_regex()


if __name__ == '__main__':
    main()
