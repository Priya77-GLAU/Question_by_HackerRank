''' Python question by HackerRank
You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and
Chemistry. The marks can be floating values. The user enters some integer N followed by the names and marks for N students.
You are required to save the record in a dictionary data type. The user then enters a student's name.
Output the average percentage marks obtained by that student, correct to two decimal places.
Input Format : The first line contains the integer N, the number of students. The next N lines contains the name and
marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.
Constraints:  2<= N <= 10, 0 <= Marks <= 100
Output Format: Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
'''

from functools import *

#############################################################################################################
def get_aver_marks_from_list(list):
    aver_val=None
    aver_val = reduce(lambda x,y: x+y, list)
    return aver_val/len(list)

#############################################################################################################
def main():

    n = int(input())
    student_marks = {}
    aver_marks=None
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # print(student_marks)
    for na in student_marks:
        if na == query_name:
            aver_marks = get_aver_marks_from_list(student_marks[na])

    print('{:.2f}'.format(aver_marks))
#############################################################################################################
main()
