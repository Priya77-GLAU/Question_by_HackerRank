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

TODO 2: Symmetric Difference
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
Input Format
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.
Output Format: Output the symmetric difference integers in ascending order, one per line.

TODO 3: No Idea
There is an array of n integers. There are also  disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i is included A, you add 1 to your happiness. If i  is included B, you add -1(minus) to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.
Constraints
1 <= n <= 10**5
1 <= m <= 10**5
1 <= any integer in the input <= 10**9
Input Format
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.
Output Format: Output a single integer, your total happiness.

TODO 4: Set .add()
Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.
Find the total number of distinct country stamps.
Input Format:
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.
Constraints: 0 < N < 1000
Output Format:  Output the total number of distinct country stamps on a single line.
Explanation:
UK and France repeat twice. Hence, the total number of distinct country stamps is 5 (five).

TODO 4: "Set .discard(), .remove() & .pop()"
You have a non-empty set S, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.

Input Format:
The first line contains integer N, the number of elements in the set S.
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Constraints 0 < n < 20,  0 < N < 20
Output Format: Print the sum of the elements of set S on a single line.
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


#TODO 2: "Symmetric Difference"
def symmetric_difference():
    len_of_list_1 = int(input())
    m_set = set([int(i) for i in input().split(' ')])
    len_of_list_2 = int(input())
    n_set = set([int(i) for i in input().split(' ')])
    answer_1 = m_set.difference (n_set)
    answer_2 = n_set.difference (m_set)
    answer_list = list(answer_1.symmetric_difference(answer_2))
    answer_list.sort()
    for i in answer_list:
        print(i)


#TODO 3: "No Idea"
def no_idea():
    array_size = tuple([int(item) for item in input().split()])
    array_list = []
    array_list = [int(i) for i in input().split(' ')]
    print(array_list)
    A_set = set([int(i) for i in input().split(' ')])
    B_set = set([int(i) for i in input().split(' ')])
    print(A_set)
    print(B_set)
    my_happiness = 0
    for i in array_list:
        if i in A_set:
            my_happiness += 1
        elif i in B_set:
            my_happiness -= 1
    print(my_happiness)
    return my_happiness


#TODO 4: "Set .add()"
def set_add():
    countries = set()
    len_of_list = int(input())
    for i in range(len_of_list):
        countries.add(input().lstrip().rstrip())
    print(len(countries))


#TODO 5: "Set .discard(), .remove() & .pop()"
def get_command():
    digits = 0
    command_str = ''
    input_list = input().lstrip().rstrip().split(' ')
    command_str = input_list[0]
    if len(input_list) == 2:
        digits = int(input_list[1])

    return command_str, digits


def discard_remove_pop():
    n = int(input())
    s = set(map(int, input().split()))

num_of_command = int(input())
for i in range(num_of_command):
    new_command, digit = get_command()
    if new_command == 'pop':
        s.pop()
    elif new_command == 'remove':
        s.remove(digit)
    elif new_command == 'discard':
        # print('command = {0}({1})'.format(new_command, digit))
        s.discard(digit)

summary_set = 0
while s:
    summary_set += s.pop()

print(summary_set)

#TODO 6:


def main():
    # set_add()
    discard_remove_pop()



if __name__ == '__main__':
    main()
