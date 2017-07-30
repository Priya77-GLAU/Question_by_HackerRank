''' Python question by HackerRank
TODO 1: "Introduction to Regex Module"
You are given a string N.
Your task is to verify that N is a floating point number.
In this task, a valid float number must satisfy all of the following requirements:
 Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
 -+4.5
 Number must contain at least 1 decimal value.
For example:
✖
 12.
✔
12.0
 Number must have exactly one . symbol.
 Number must not give any exceptions when converted using float(N).
Input Format:
The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.
Constraints: 0 < T < 10
Output Format: Output True or False for each test case.

TODO 2: "Re.split()"
You are given a string S, containing , and/or . and 0-9 digits.
Your task is to re.split() all of the , and . symbols.
Input Format: A single line of input containing the string S.
Output Format: Print the numbers obtained after splitting the string on separate lines.

TODO 3: "Group(), Groups() & Groupdict()"
You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in  S(read from left to right) that has consecutive repetitions.
Input Format: A single line of input containing the string S.
Constraints: 0 < len(S) < 100
Output Format: Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

TODO 4: "Re.findall() & Re.finditer()"
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.
Note :
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.
Input Format: A single line of input containing string S.
Constraints: 0 < len(S) < 100
Output Format: Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print -1.

'''

import re


# TODO 1: "Introduction to Regex Module"
def string_from_dot(input_line):
    if input_line.isdigit():
        # print(input_line, end=' is ')
        print('True')
        return 0
    else:
        # print(input_line, end=' is ')
        print('False')
        return 0


def check_number(input_line):
    if input_line[0] == '+' or input_line[0] == '-':
        input_line = input_line[1:]
    if input_line[0] == '.':
        string_from_dot(input_line[1:])
        return 0
    else:
        input_list = input_line.split('.')
        if len(input_list) != 2:
            # print(input_line, end=' is ')
            print('False')
            return 0
        else:
            if input_list[0].isdigit() and input_list[1].isdigit():
                # print(input_line, end=' is ')
                print('True')
                return 0
            else:
                # print(input_line, end=' is ')
                print('False')
                return 0


def introduction_to_regex():
    number_of_tests = int(input().lstrip().rstrip())
    for _ in range(int(number_of_tests)):
        input_line = input().lstrip().rstrip()
        check_number(input_line)


# TODO 2: "Re.split()"
# s = input().lstrip().rstrip()
# pattern = re.compile(r'[,.]+')
# s_list = re.split(pattern, s)
# for str in s_list:
#     if len(str):
#         print(str)


# TODO 3: "Group(), Groups() & Groupdict()"
# source_s = input().lstrip().rstrip()
# pattern = re.compile(r'\w+')
# s_list = re.search('[\w]+', source_s)
# result = list(filter(lambda x: re.search(x, source_s), [s * 2 for s in source_s if s.isalnum()]))
# if len(result):
#     print(result[0][0])
# else:
#     print(-1)


# TODO 4: "Re.findall() & Re.finditer()"
source_s = input().lstrip().rstrip()
not_result = True
pattern = re.compile(r'[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM][AEIOUaeiou][AEIOUaeiou]+[qwrtypsdfghjklzxcvbnm'
                     r'QWRTYPSDFGHJKLZXCVBNM]')
match = re.search(pattern, source_s)
while match:
    # text_pos = match.span()
    # print('match.end =', match.end())
    find_str = re.findall(r'[AEIOUaeiou][AEIOUaeiou]+', source_s[match.start():match.end()])
    if len(find_str[0]):
        not_result = False
        print(find_str[0])

    source_s = source_s[match.end() - 1:]
    # print(source_s[match.start():match.end()])
    match = re.search(pattern, source_s)

if not_result:
    print(-1)


def main():
    # introduction_to_regex()
    pass


if __name__ == '__main__':
    main()
