''' Python question by HackerRank
TODO 1:
You are given a 2-D array with dimensions NxM.
Your task is to perform the  tool over axis 0 and then find the Product of that result.
Input Format:
The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.
Output Format: Compute the sum along axis 0. Then, print the product of that sum.

TODO 2:
You are given a 2-D array with dimensions NxM.
Your task is to perform the min function over axis 1 and then find the max of that.
Input Format:
The first line of input contains the space separated values of N and M.
The next N lines contains M space separated integers.
Output Format: Compute the min along axis 1 and then print the max of that result.

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



#TODO 1: "Sum and Prod" (Numpy)
def sum_and_prod():
    # array_size = tuple([int(item) for item in input().split()])
    # array_list = []
    # for i in range(array_size[0]):
    #     array_list.append(tuple([int(item) for item in input().split()]))

    # my_array = numpy.array(array_list)
    my_array = get_array_from_input()
    step_1 = numpy.sum(my_array, axis = 0)
    print (step_1)
    print(numpy.prod(step_1))
    return 0


#TODO 2: "Min and Max" (Numpy)
def min_and_max():
    my_array = get_array_from_input()
    step_1 = numpy.min(my_array, axis=1)
    print(numpy.max(step_1))
    return 0



def main():
    # sum_and_prod()
    min_and_max()




if __name__ == '__main__':
    main()
