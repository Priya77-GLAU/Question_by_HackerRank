''' Python question by HackerRank
TODO 1:
"collections.Counter()"
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay X amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.
Input Format
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the  desired by the customer and , the price of the shoe.
Constraints
0 < X < 10**3
0 < N <= 10**3
20 < x_i < 100
2 < shoe_size < 20
Output Format: Print the amount of money earned by Raghu .

TODO 2:
"DefaultDict Tutorial"

TODO 3: "collections_namedtuple"
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
Your task is to help Dr. Wesley calculate the average marks of the students.
Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)
Input Format:
The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the MARKS, ID, NAME and CLASS , under their respective column names.
Constraints: 0 < N <= 100
Output Format:
Print the average marks of the list corrected to 2 decimal places.

# TODO 4: "Collections.OrderedDict()"

# TODO 5: "Word Order"
You are given N words. Some words may repeat. For each word, output its number of occurrences. The output order should
correspond with the input order of appearance of the word. See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.
Constraints:
1 <= N <= 1**5
The sum of the lengths of all the words do not exceed 10**6
All the words are composed of lowercase English letters only.
Input Format
The first line contains the integer, N.
The next N lines each contain a word.
Output Format
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words
appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

# TODO 6:
"Collections.deque()"
Perform append, pop, popleft and appendleft methods on an empty deque .
Input Format:
The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.
Constraints: 0 < N <=100
Output Format: Print the space separated elements of deque d.

TODO 7:
"Piling Up"
There is a horizontal row of N cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube_i is on top of cube_j then side_length_j >= side_length_i .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains N, the number of cubes.
The second line contains N space separated integers, denoting the sideLengths of each cube in that order.
Constraints: 1<= T <= 5
1 <= N <= 10**5
1 <= sideLengths  < 2**31
Output Format:
For each test case, output a single line containing either "Yes" or "No" without the quotes.

'''

from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import OrderedDict
from collections import deque


# TODO 1: "collections.Counter()"
def get_size_and_price():
    input_list = input().lstrip().rstrip().split(' ')
    return int(input_list[0]), int(input_list[1])


def collections_counter():
    num_of_shoes = int(input())
    shoe_size_list = Counter([int(x) for x in input().lstrip().rstrip().split(' ')])
    num_of_customers = int(input())
    money = 0
    for i in range(num_of_customers):
        size, price = get_size_and_price()
        if shoe_size_list[size] > 0:  # size in shoe_size_list
            shoe_size_list[size] -= 1
            money += price
    print(money)


# TODO 2: "DefaultDict Tutorial"
def default_dict_tutorial():
    n, m = [int(x) for x in input().lstrip().rstrip().split(' ')]
    group_a = []
    for i in range(n):
        group_a.append(input().lstrip().rstrip())

    for word_i in range(m):
        word_group_b = input().lstrip().rstrip()
        if word_group_b in group_a:  # len([x for x in group_a if x == word_group_b])
            for i, ch in enumerate(group_a, 1):
                if ch == word_group_b:
                    print(i, end=' ')
                else:
                    pass
            print()
        else:
            print('-1')

            # result = defaultdict(list)
            # for word_i in range(m):
            #     word_group_b = input().lstrip().rstrip()
            #     if word_group_b in group_a:
            #         for i,ch  in enumerate(group_a, 1):
            #             if ch == word_group_b:
            #                 result[word_group_b].append(i)
            #             else:
            #                 pass
            #     else:
            #         result[word_group_b].append('-1')
            #     print(result)


# TODO 3: "collections_namedtuple"
def collections_namedtuple():
    student_list = []
    num_of_students = int(input())
    header_list = [x for x in input().split(' ') if x]
    Student = namedtuple('Student', 'MARKS ID NAME CLASS')
    # d = defaultdict(list)
    for _ in range(num_of_students):
        input_list = [x for x in input().split(' ') if x]
        for n, v in zip(header_list, input_list):
            if n == 'MARKS':
                st_marks = v
            elif n == 'ID':
                st_id = v
            elif n == 'NAME':
                st_name = v
            elif n == 'CLASS':
                st_clas = v
        one_student = Student(ID=st_id, MARKS=int(st_marks), NAME=st_name, CLASS=st_clas)
        student_list.append(one_student)
    count = 0
    sum_of_marks = 0
    for stud in student_list:
        count += 1
        sum_of_marks += stud.MARKS
    print('{:.2f}'.format(sum_of_marks / len(student_list)))
    return 0


# TODO 4: "Collections.OrderedDict()"
def get_name_and_price():
    *names, price = [x for x in input().split(' ') if x]
    return ' '.join(names), int(price)


def collections_ordered_dict():
    ordered_dictionary = OrderedDict()
    num_of_line = int(input())

    # name = ' '.join([x for x in input().split(' ') if x])
    # print(name)
    # ordered_dictionary[name] = 1

    for _ in range(num_of_line):
        item_name, net_price = get_name_and_price()

        ordered_dictionary[item_name] = ordered_dictionary.get(item_name, 0) + net_price

    for item_order in ordered_dictionary:
        print('{} {}'.format(item_order, ordered_dictionary[item_order]))

    return 0


# TODO 5: "Word Order"
def word_ordered_dict():
    list_of_words = OrderedDict()
    num_of_words = int(input())
    for _ in range(num_of_words):
        word = ''.join(input().lstrip().rstrip().split(' '))
        list_of_words[word] = list_of_words.get(word, 0) + 1
    print(len(list_of_words))
    result = []
    for item in list_of_words.values():
        print(item, end=' ')
    return 0


# TODO 6: "Collections.deque()"
def get_command():
    digits = 0
    command_str = ''
    input_list = input().lstrip().rstrip().split(' ')
    command_str = input_list[0]
    if len(input_list) == 2:
        digits = int(input_list[1])
    return command_str, digits


def collections_deque():
    num_of_command = int(input())
    d = deque()
    for _ in range(num_of_command):
        new_command, digit = get_command()
        if new_command == 'append':
            d.append(digit)
        elif new_command == 'appendleft':
            d.appendleft(digit)
        elif new_command == 'pop':
            # print('command = {0}({1})'.format(new_command, digit))
            d.pop()
        elif new_command == 'popleft':
            d.popleft()
    while d:
        print(d.popleft(), end=' ')
    return 0


# TODO 7: "Piling Up"
def split_cubes(row_of_cubes):
    side_left = []
    side_rigft = []
    if len(row_of_cubes) % 2 == 1:
        side_left.append(row_of_cubes.pop(0))
    else:
        pass
    while len(row_of_cubes):
        side_rigft.append(row_of_cubes.pop(0))
        side_left.append(row_of_cubes.pop(0))
    return side_left, side_rigft


def is_build_pile_from_2sides(side_left, side_right):
    result = True
    while len(side_left) + len(side_right) > 0:
        pass
    return result


def is_build_pile(list_of_cubes):
    result = True
    pile_of_cube = []
    end_item = None
    for i in range(0, len(list_of_cubes) - 1, 2):
        if len(list_of_cubes[i]) == 1:
            print(end_item)
            print(list_of_cubes[i])
            if end_item is None:
                return True
            else:
                # end_item = pile_of_cube.pop()
                if list_of_cubes[i] > end_item:
                    return False
                else:
                    # pile_of_cube.append(end_item)
                    # pile_of_cube.append(list_of_cubes[i])
                    return True

        elif len(list_of_cubes[i]) == 2:
            if max_int(list_of_cubes[i], list_of_cubes[i + 1]) > end_item:
                return False
            else:
                return True
        else:
            end_item = list_of_cubes[i + 2]
            if end_item > max_int(list_of_cubes[i], list_of_cubes[i + 1]):
                return False
            else:
                if list_of_cubes[i] > list_of_cubes[i + 1]:
                    end_item = list_of_cubes[i]
                else:
                    end_item = list_of_cubes[i + 1]
            continue
    return result
    # elif list_of_cubes[i] > list_of_cubes[i+1]:
    #     pile_of_cube.append(end_item)
    #     pile_of_cube.append(list_of_cubes[i+1])
    #     pile_of_cube.append(list_of_cubes[i])
    #     return True
    # else:
    #     pile_of_cube.append(end_item)
    #     pile_of_cube.append(list_of_cubes[i])
    #     pile_of_cube.append(list_of_cubes[i+1])
    #     return True

    # else:
    #     if list_of_cubes[i+2] > max_int(list_of_cubes[i], list_of_cubes[i+1]):
    #         return False
    #     else:
    #         if list_of_cubes[i] > list_of_cubes[i+1]:
    #             pile_of_cube.append(list_of_cubes[i+1])
    #             pile_of_cube.append(list_of_cubes[i])
    #         else:
    #             pile_of_cube.append(list_of_cubes[i])
    #             pile_of_cube.append(list_of_cubes[i+1])

    # while len(list_of_cubes):
    #     i = list_of_cubes.pop(0)
    #     j = list_of_cubes.pop(0)


def max_int(int_1, int_2):
    if int_1 > int_2:
        return int_1
    else:
        return int_2


def is_build_pile_by_deque(list_of_cubes):
    result = True
    end_item = None
    left_item = None
    right_item = None
    # print('len(list_of_cubes) ->', len(list_of_cubes))
    while len(list_of_cubes) > 0:
        # print(list_of_cubes, 'is size ', len(list_of_cubes))
        # print('list_of_cubes is size ', len(list_of_cubes))
        # print('end_item ->', end_item)
        if len(list_of_cubes) == 1:
            left_item = list_of_cubes.popleft()
            # print('left_item ->', left_item)
            if left_item > end_item:
                print('last item > end_item')
                return False
            else:
                return True
        elif len(list_of_cubes) == 2:
            if end_item is None:
                return True
            else:
                left_item = list_of_cubes.popleft()
                right_item = list_of_cubes.pop()
                if left_item > end_item or right_item > end_item:
                    if left_item > end_item:
                        print('left_item > end_item', left_item, ' >', end_item)
                        print()
                    else:
                        print('right_item > end_item', right_item, ' >', end_item)
                    return False
                else:
                    return True
        else:
            left_item = list_of_cubes.popleft()
            right_item = list_of_cubes.pop()
            if left_item < right_item:
                end_item = left_item
            else:
                end_item = right_item
            continue
    return result


def is_build_pile_by_deque_v2(list_of_cubes):
    result = True
    end_item = None
    left_item = None
    right_item = None
    while len(list_of_cubes) > 0:
        if len(list_of_cubes) == 1:
            # print('list_of_cubes is', len(list_of_cubes))
            left_item = list_of_cubes.popleft()
            if left_item > end_item:
                # print('last item > end_item')
                return False
            else:
                return True
        else:
            left_item = list_of_cubes.popleft()
            right_item = list_of_cubes.pop()
            if left_item > right_item:
                new_item = left_item
                list_of_cubes.append(right_item)
            else:
                new_item = right_item
                list_of_cubes.appendleft(left_item)
            # print('new_item =', new_item, 'end_item =', end_item)
            if end_item is None:
                end_item = new_item
                continue
            elif new_item > end_item:
                # print('new_item > end_item ...', new_item, '>', end_item)
                return False
            else:
                continue
    return True


def piling_up():
    number_of_tests = int(input().lstrip().rstrip())
    for _ in range(number_of_tests):
        num_of_cubes = input().lstrip().rstrip()
        number_of_cubes = int(num_of_cubes)

        row_of_cubes = deque([int(x) for x in input().split(' ') if x], number_of_cubes)
        len_of_cubes = len(row_of_cubes)
        if is_build_pile_by_deque_v2(row_of_cubes):
            print(len_of_cubes, ' -> Yes')
            # print ('Yes')
        else:
            # print ('No')
            print(len_of_cubes, ' -> No')

    return 0


def main():
    # collections_counter()
    # default_dict_tutorial()
    # collections_namedtuple()
    # collections_ordered_dict()
    # word_ordered_dict()
    # collections_deque()
    piling_up()


if __name__ == '__main__':
    main()
