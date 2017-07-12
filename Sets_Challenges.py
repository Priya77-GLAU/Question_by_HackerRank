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

TODO 6:
"Set .union() Operation"
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only
to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is
subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of
students who have subscribed to at least one newspaper.
Input Format
The first line contains an integer, N, the number of students who have subscribed to the English newspaper.
The second line contains N space separated roll numbers of those students.
The third line contains B, the number of students who have subscribed to the French newspaper.
The fourth line contains B space separated roll numbers of those students.
Constraints: 0 < Total number of students in college < 1000
Output Format: Output the total number of students who have at least one subscription.

TODO 7:Set .intersection() Operation

TODO 8: "Set .difference() Operation"

TODO 9: "Set .symmetric_difference() Operation"

TODO 10: "Set Mutations"

TODO 11: "The Captain's Room"
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of K members per group where K ≠ 1.
The Captain was given a separate room, and the rest were given one room per group.
Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear K times per group except for the Captain's room.
Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.
Input Format
The first line consists of an integer, K, the size of each group.
The second line contains the unordered elements of the room number list.
1 < K < 1000
Output Format: Output the Captain's room number.
Explanation
The list of room numbers contains 31 elements. Since K is 5, there must be 6 groups of families. In the given list, all of the numbers repeat 5 times except for room number 8.
Hence,  is the Captain's room number.

TODO 12: "Check Subset"
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.
If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
Input Format:
The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set B.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.
Constraints
0 < T < 21
0 < number of elements in each set < 1001
Output Format: Output True or False for each test case on separate lines.

TODO 13: "Check Strict Superset"
You are given a set A and N other sets.
Your job is to find whether set A is a strict superset of each of the N sets.
Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.
Example
Set([1,3,4]) is a strict superset of set([]).
Set([1,3,4]) is not a strict superset of set([1,3,4]).
Set([1,3,4]) is not a strict superset of set([1,3,5]).
Input Format
The first line contains the space separated elements of set A.
The second line contains integer N, the number of other sets.
The next N lines contains the space separated elements of the other sets.
Constraints
0 < len(set A) < 501
0 < N < 21
0 < len(other sets) < 101
Output Format: Print True if set A is a strict superset of all other N sets. Otherwise, print False.
Set A is the strict superset of the set but not of the set because  is not in set .
Hence, the output is False.
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
    return 0


#TODO 6: "Set .union() Operation"
def union_operation():
    n = int(input())
    english_subscribe = set(map(int, input().split()))
    b = int(input())
    french_subscribe = set(map(int, input().split()))
    print(len(english_subscribe.union(french_subscribe)))


#TODO 7: "Set .intersection() Operation"
def intersection_operation():
    n = int(input())
    english_subscribe = set(map(int, input().split()))
    b = int(input())
    french_subscribe = set(map(int, input().split()))
    print(len(english_subscribe.intersection(french_subscribe)))
    return 0


#TODO 8: "Set .difference() Operation"
def difference_operation():
    n = int(input())
    english_subscribe = set(map(int, input().split()))
    b = int(input())
    french_subscribe = set(map(int, input().split()))
    print(len(english_subscribe.difference(french_subscribe)))


#TODO 9: "Set .symmetric_difference() Operation"
def symmetric_difference_operation():
    n = int(input())
    english_subscribe = set(map(int, input().split()))
    b = int(input())
    french_subscribe = set(map(int, input().split()))
    print(len(english_subscribe.symmetric_difference(french_subscribe)))


#TODO 10: "Set Mutations"
def set_mutations():
    size_a = int(input())
    a_set = set(map(int, input().lstrip().rstrip().split()))
    numbers_of_command = int(input())
    for i in range(numbers_of_command):
        new_command, digit = get_command()
        other_set = set(map(int, input().lstrip().rstrip().split()))
        # print('{} {} for {}'.format(new_command, digit, other_set))
        if new_command == 'intersection_update':
            a_set = a_set.intersection(other_set)

        elif new_command == 'update':
            a_set.update(other_set)

        elif new_command == 'symmetric_difference_update':
            a_set = a_set.symmetric_difference(other_set)

        elif new_command == 'difference_update':
            a_set = a_set.difference(other_set)

    print(sum(a_set))


#TODO 11: "The Captain's Room"
def captains_room():
    num_of_group = int(input())
    rooms_list = list(input().lstrip().rstrip().split())
    rooms_dict = {}
    for i in rooms_list:
        if i in rooms_dict:
            rooms_dict[i] += 1
        else:
            rooms_dict[i] = 1
    captains_room = [x for x in rooms_dict if rooms_dict[x] == 1]
    print(int(captains_room[0]))
    return 0


#TODO 12: "Check Subset"
def check_subset():
    num_of_tests = int(input())
    for i in range(num_of_tests):
        size_a = int(input())
        set_a = set(list(input().lstrip().rstrip().split()))
        size_b = int(input())
        set_b = set(list(input().lstrip().rstrip().split()))
        print(set_a == set_a.intersection(set_b))
    return 0


#TODO 13: "Check Strict Superset"
def is_strict_superset(super_set, sub_set):
    if len(super_set) > len(sub_set) and super_set.issuperset(sub_set):
        return True
    else:
        return False


def check_strict_superset():
    super_set_a = set(list(input().lstrip().rstrip().split()))
    num_of_sets = int(input())
    result = True
    for i in range(num_of_sets):
        set_b = set(list(input().lstrip().rstrip().split()))
        result = result and is_strict_superset(super_set_a, set_b)
    print(result)
    return 0


def main():
    # set_add()
    # discard_remove_pop()
    # union_operation()
    # intersection_operation()
    # difference_operation()
    # symmetric_difference_operation()
    # set_mutations()
    # captains_room()
    # check_subset()
    check_strict_superset()


if __name__ == '__main__':
    main()
