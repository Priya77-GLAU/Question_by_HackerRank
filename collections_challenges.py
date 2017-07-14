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


'''

from collections import Counter
from collections import defaultdict
from collections import namedtuple


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

def main():
    # collections_counter()
    # default_dict_tutorial()
    collections_namedtuple()


if __name__ == '__main__':
    main()
