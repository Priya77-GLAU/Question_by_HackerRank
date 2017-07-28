''' Python question by HackerRank
TODO 1: "Zipped!"
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.
Average score = sum of score obtained in all subjects by a student / total number of subjects
The format for the general mark sheet is:
Student ID → ___1_____2_____3_____4_____5__
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5
Input Format
The first line contains N and X separated by a space.
The next X lines contains the space separated marks obtained by students in a particular subject.
Constraints:
Output Format
Print the averages of all students on separate lines.
The averages must be correct up to 1 decimal place.


'''

from fractions import Fraction
from functools import reduce
import re
import sys

# TODO 1: "Zipped!"
stud, subjects = input().lstrip().rstrip().split(' ')
input_list = []
for _ in range(int(subjects)):
    input_line = input().lstrip().rstrip().split(' ')
    input_list.append([float(x) for x in input_line])
for x in zip(*input_list):
    print(round(sum(x) / len(x), 1))


def main():
    pass

if __name__ == '__main__':
    main()
