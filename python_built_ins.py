''' Here I continue to solve the chellenges by HackerRank
'''

import sys
from operator import attrgetter


# TODO 1 "Python Evaluation"
# eval(input().strip())

# TODO 2 "Athlete Sort"
def by_second_item(item):
    return item[1]


k = 0


def by_k_item(item):
    return item[k]


def print_arr(arr):
    for item in arr:
        print(' '.join(map(str, item)))


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
arr = []
for arr_i in range(n):
    arr_1 = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_1)
k = int(input().strip())

sorted_arr = sorted(arr, key=by_k_item)
print_arr(sorted_arr)
