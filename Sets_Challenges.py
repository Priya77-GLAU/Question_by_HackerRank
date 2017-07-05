''' Python question by HackerRank
TODO 1:
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
Formula used: Average = sum of distinct heights / total number of distinct heights
Input Format:
The first line contains the integer, N, the total number of plants.
The second line contains the N space separated heights of the plants.
Constraints: 0  < N <= 100
Output Format:
Output the average height value on a single line.

TODO 2:

'''

import numpy
import sys


def get_array_from_input():
    array_size = tuple([int(item) for item in input().split()])
    array_list = []
    for i in range(array_size[0]):
        array_list.append(tuple([int(item) for item in input().split()]))

    new_array = numpy.array(array_list)
    return new_array



#TODO 1: "Introduction to Sets"
def average(array):
    # len_of_string = int(input())
    # value_list = [int(i) for i in input().split(' ')]
    # array = set(value_list)
    # print(sum(array)/len(array))
    array = set(array)
    return sum(array) / len(array)


def main():
    # sum_and_prod()
    # min_and_max()
    # mean_var_std()
    # dot_cross()
    # print(my_array)




if __name__ == '__main__':
    main()
