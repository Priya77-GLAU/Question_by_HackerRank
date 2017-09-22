''' Python question by HackerRank
TODO 1: "Exceptions"
You have to pass all the testcases to get a positive score.
'''

import re


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


# TODO 2: "Incorrect Regex"
def incorrect_regex():
    number_of_tests = int(input().lstrip().rstrip())
    test_str = 'QWRTYPSDFGHJKLZXCVBNMAEIOU11223344556677889900 QWRTYPSDFGHJKLZXCVBNMAEIOU11223344556677889900'
    for _ in range(int(number_of_tests)):
        ss = input().lstrip().rstrip()
        try:
            match = ''.join(re.findall(ss, test_str))
        except Exception:
            print('False')
        else:
            print('True')



if __name__ == '__main__':
    incorrect_regex()

