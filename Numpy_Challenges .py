''' Python question by HackerRank
TODO 1:
You are given a 2-D array with dimensions NxM.
Your task is to perform the  tool over axis 0 and then find the Product of that result.
Input Format:
The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.
Output Format: Compute the sum along axis 0. Then, print the product of that sum.

'''

import numpy
import sys


#TODO 1:
array_size = tuple([int(item) for item in input().split()])
array_list = []
for i in range(array_size[0]):
    array_list.append(tuple([int(item) for item in input().split()]))

my_array = numpy.array(array_list)

step_1 = numpy.sum(my_array, axis = 0)
print (step_1)         #Output : [4 6]
print(numpy.prod(step_1))




# def main():



# if __name__ == '__main__':
#     main()
