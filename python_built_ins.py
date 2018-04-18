''' Here I continue to solve the chellenges by HackerRank
'''

import sys
from operator import attrgetter
import re
from functools import reduce


# TODO 1 "Python Evaluation"
# eval(input().strip())

# TODO 2 "Athlete Sort"
# def by_second_item(item):
#     return item[1]
#
# k = 0
# def by_k_item(item):
#     return item[k]
#
# def print_arr(arr):
#     for item in arr:
#         print(' '.join(map(str, item)))
#
# n, m = input().strip().split(' ')
# n, m = [int(n), int(m)]
# arr = []
# for arr_i in range(n):
#     arr_1 = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#     arr.append(arr_1)
# k = int(input().strip())
# sorted_arr = sorted(arr, key=by_k_item)
# print_arr(sorted_arr)

# TODO 3 "Any or All"
# numbers = input().strip().split(' ') if int(input().strip()) else None
# print(all(list(map(lambda x: int(x) > 0, numbers))) and any(list(map(lambda x: str(x) == str(x)[::-1], numbers))))

# TODO 4 "ginortS"
def separete_digits_1(str):
    if str.isdigit() and int(str) % 2 == 1:
        return True
    return False


def separete_digits_2(str):
    if str.isdigit() and int(str) % 2 == 0:
        return True
    return False


upp_chs = 'BCDFGHJKLMNPQRSTVWXZYAEIOU'
lower_chs = 'bcdfghjklmnpqrstvwxzyaeiou'
inp_str = input().strip()

result_digit_part_1 = list(filter(lambda x: separete_digits_1(x), inp_str))
result_digit_part_2 = list(filter(lambda x: separete_digits_2(x), inp_str))
result_lower_part = list(filter(lambda x: x in 'bcdfghjklmnpqrstvwxzyaeiou', inp_str))
result_upper_part = list(filter(lambda x: x in 'BCDFGHJKLMNPQRSTVWXZYAEIOU', inp_str))

result_lower_part, result_upper_part, result_digit_part_1, result_digit_part_2 = list(
    map(sorted, [result_lower_part, result_upper_part, result_digit_part_1, result_digit_part_2]))
result_list = result_lower_part + result_upper_part + result_digit_part_1 + result_digit_part_2
result_str = reduce(lambda x, y: x + y, result_list)
print(result_str)
