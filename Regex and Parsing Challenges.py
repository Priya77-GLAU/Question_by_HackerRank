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

TODO 5: "Re.start() & Re.end()"
You are given a string S.
Your task is to find the indices of the start and end of string K in S.
Input Format:
The first line contains the string S.
The second line contains the string K.
Constraints: 0 < len(s) < 100, 0 < len(k) < len(s)
Output Format:
Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

TODO 6: "Regex Substitution"
You are given a text of  lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:
&& → and
|| → or
Both && and || should have a space " " on both sides.
Input Format: The first line contains the integer, N.
The next N lines each contain a line of the text.
Constraints: 0 < N < 100
Neither && nor || occur in the start or end of each line.
Output Format: Output the modified text.

# TODO 7: "Validating Roman Numerals"
You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.
Input Format: A single line of input containing a string of Roman characters.
Output Format: Output a single line containing True or False according to the instructions above.
Constraints: The number will be between 1 and 3999 (both included).

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
# source_s = input().lstrip().rstrip()
# not_result = True
# pattern = re.compile(r'[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM][AEIOUaeiou][AEIOUaeiou]+[qwrtypsdfghjklzxcvbnm'
#                      r'QWRTYPSDFGHJKLZXCVBNM]')
# match = re.search(pattern, source_s)
# while match:
#     # text_pos = match.span()
#     # print('match.end =', match.end())
#     find_str = re.findall(r'[AEIOUaeiou][AEIOUaeiou]+', source_s[match.start():match.end()])
#     if len(find_str[0]):
#         not_result = False
#         print(find_str[0])
#
#     source_s = source_s[match.end() - 1:]
#     # print(source_s[match.start():match.end()])
#     match = re.search(pattern, source_s)
#
# if not_result:
#     print(-1)


# TODO 5: "Re.start() & Re.end()"
# not_result = True
# new_start = 0
# source_s = input().lstrip().rstrip()
# source_k = input().lstrip().rstrip()
# if len(source_k) == 1:
#     match = re.search(source_k, source_s)
#     while match:
#         # print('match.end =', match.end())
#         not_result = False
#         print((match.start() + new_start, match.end() - 1 + new_start))
#         new_start += match.end() + 1
#         match = re.search(source_k, source_s[new_start:])
#
# else:
#     match = re.search(source_k, source_s)
#     while match:
#         # print('match.end =', match.end())
#         not_result = False
#         print((match.start() + new_start, match.end() - 1 + new_start))
#         new_start += match.end() - 1
#         match = re.search(source_k, source_s[new_start:])
# if not_result:
#     print((-1, -1))

# TODO 6: "Regex Substitution"
# number_of_str = int(input().lstrip().rstrip())
# for _ in range(number_of_str):
#     source_s = input()
#     pattern = re.compile(r'#')
#     if re.match(pattern, source_s):
#         print(source_s)
#     else:
#         # source_s = replace_2_and(source_s)
#         # source_s = replace_2_or(source_s)
#         re_sub = True
#         while re_sub:
#             # print(source_s)
#             new_source = re.sub(" && ", " and ", source_s)
#             if new_source == source_s:
#                 re_sub = False
#             else:
#                 source_s = new_source
#         re_sub = True
#         while re_sub:
#             new_source = re.sub(" \|\| ", " or ", source_s)
#             if new_source == source_s:
#                 re_sub = False
#             else:
#                 source_s = new_source
#         print(source_s)



# TODO 7: "Validating Roman Numerals"
def valid_roman_numerals():
    source_s = input().lstrip().rstrip()

    pattern = re.compile(r'[CDLXIVƆM]+')
    match = re.match(pattern, source_s)
    if match.group(0) != source_s:
        print('False')
        return 1
    pattern = re.compile(r'[XV]I{4}')
    match = re.search(pattern, source_s)
    # print(match)
    # print(match.group(0))
    if match:
        print('False')
        return 1
    pattern = re.compile(r'X{4}')
    match = re.search(pattern, source_s)
    if match:
        print('False')
        return 1
    pattern = re.compile(r'C{4}')
    match = re.search(pattern, source_s)
    if match:
        print('False')
        return 1
    pattern = re.compile(r'M{4}')
    match = re.search(pattern, source_s)
    if match:
        print('False')
        return 1
    pattern = re.compile(r'L{2}')
    match = re.search(pattern, source_s)
    if match:
        print('False')
        return 1

    print('True')
    return 0


def main():
    # introduction_to_regex()
    valid_roman_numerals()


if __name__ == '__main__':
    main()
