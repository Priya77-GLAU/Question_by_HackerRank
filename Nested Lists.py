''' Python question by HackerRank
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the
name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.
Constraints  2<= N <=5
There will always be one or more students having the second lowest grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order
their names alphabetically and print each one on a new line.

Explanation
There are  students in this class whose names and grades are assembled to build the following list:
...
The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order
their names alphabetically and print each name on a new line.
'''

def find_second_val_in_list(list_var):
    sec_val=float(100)
    min_val=float(100)
    for i in list_var:
        if i[1] < min_val:
            sec_val=min_val
            min_val=i[1]
        elif i[1] > min_val and i[1] < sec_val:
            sec_val=i[1]
        else:
            pass
        # print('min_val =', min_val, 'sec_val =', sec_val)
    return sec_val

def get_student_list_for_grade(stud_list, grade):
    stu_list=[]
    for i in stud_list:
        # print(i)
        # print(grade)
        if grade == i[1]:
            # print(i[1], '==', grade)
            stu_list.append(i[0])
            # print('stu_list =', stu_list)

    return stu_list

students = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

second_grade=find_second_val_in_list(students)
lst=get_student_list_for_grade(students, second_grade)
lst.sort()
for i in lst:
    print(i)