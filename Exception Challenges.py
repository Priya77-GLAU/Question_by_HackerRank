''' Python question by HackerRank
TODO 1: "Exceptions"
You have to pass all the testcases to get a positive score.
'''

import email.utils
import re
from functools import reduce


# TODO 1: "Exceptions"
def exceptions_example():
    number_of_tests = int(input().lstrip().rstrip())
    for _ in range(int(number_of_tests)):
        try:
            a, b = [int(i) for i in input().lstrip().rstrip().split()]
        except ValueError as e:
            print("Error Code:",e)
            continue

        try:
            print(a//b)
        except ZeroDivisionError as e:
            print("Error Code:",e)



if __name__ == '__main__':
    exceptions_example()
