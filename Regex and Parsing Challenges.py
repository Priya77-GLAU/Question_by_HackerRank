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
You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True.
Otherwise, print False. Try to create a regular expression for a valid Roman numeral.
Input Format: A single line of input containing a string of Roman characters.
Output Format: Output a single line containing True or False according to the instructions above.
Constraints: The number will be between 1 and 3999 (both included).

# TODO 8: "Validating phone numbers"
Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check
whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a 7,8 or 9.
Concept
A valid mobile number is a ten digit number starting with a 7,8 or 9.
Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available
here. You could also go through the link below to read more about regular expressions in Python.
Input Format:
The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.
Output Format:
For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines.
Do not print the quotes.

# TODO 9: "Validating and Parsing Email Addresses"
A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is 1, 2, or 3 characters in length.
Given Т pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
Hint: Try using Email.utils() to complete this challenge. For example, this code:
import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
produces this output:
('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>
Input Format
The first line contains a single integer, N, denoting the number of email address.
Each line i of the N subsequent lines contains a name and an email address as two space-separated values following this format:
name <user@email.com>
Output Format:
Print the space-separated name and email address pairs containing valid email addresses only. Each pair must be printed on a new line in the following format:
name <user@email.com>

# TODO 10: "Validating UID"
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.
A valid UID must follow the rules below:
It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (a - z,A  - Z & 0 - 9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
Input Format: The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.
Output Format:
For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

# TODO 11: "Validating Credit Card Numbers"
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
A valid credit card from ABCD Bank has the following characteristics:
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
Input Format
The first line of input contains an integer N.
The next N lines contain credit card numbers.
Output Format
Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

# TODO 12: "Validating Postal Codes"
A postal code P must be a number in the range of (100000-999999).
A postal code P must not contain more than one alternating repetitive digit pair.
Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
For example:
121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.
Your task is to validate whether  is a valid postal code or not.
Input Format
One single line of input containing the string P.
Output Format
Print "True" if  is valid. Otherwise, print "False". Do not print the quotation marks.
Sample Input 0
110000
Sample Output 0
False
Explanation 0
1 1 0O0O : (0, 0) and (O, O) are two alternating digit pairs. Hence, it is an invalid postal code.
Note:
A score of 0 will be awarded for using 'if' conditions in your code.
You have to pass all the testcases to get a positive score.
'''

import email.utils
import re
from functools import reduce


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


# TODO 8: "Validating phone numbers"
def valid_phone_numbers():
    number_of_str = int(input().lstrip().rstrip())
    for _ in range(number_of_str):
        source_s = input().lstrip().rstrip()
        # print(source_s)
        pattern = re.compile(r'[789]')
        if re.match(pattern, source_s):
            if len(source_s) != 10:
                print('NO')
                continue
            pattern = re.compile(r'\D')
            if re.search(pattern, source_s):
                print('NO')
                continue
            print('YES')
            continue
        else:
            print('NO')
            continue
    return 0


# TODO 9: "Validating and Parsing Email Addresses"
def valid_email_name(email_name):
    # pattern = re.compile(r'[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNMAEIOUaeiou]')
    # if re.match(pattern, email_name):
    if email_name[0] in 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNMAEIOUaeiou':
        match = ''.join(re.findall(r'[\W]', email_name, re.VERBOSE))
        match = ''.join(re.findall(r'[^_]', match))
        match = ''.join(re.findall(r'[^-]', match))
        match = ''.join(re.findall(r'[^\.]', match))
        if match:
            return 1
        else:
            return 0
    else:
        # print('NO')
        return 1


def valid_email_domain(new_email_name, email_name):
    match = re.search(new_email_name + '@', email_name)
    new_email_domain = email_name[match.end():]
    match = re.findall(r'[\.]', new_email_domain)
    if len(match) != 1:
        return 1
    else:
        new_email_domain_name, new_email_domain_extension = new_email_domain.split('.')
        first_ch = new_email_domain_name[0]
        if first_ch == '"' or first_ch == '<':
            new_email_domain_name = new_email_domain_name[1:]
        # print(new_email_domain_name)
        if not new_email_domain_name.isalpha():
            return 1
        else:
            last_ch = new_email_domain_extension[len(new_email_domain_extension) - 1]
            if last_ch == '"' or last_ch == '>':
                new_email_domain_extension = new_email_domain_extension[:-1:]
            if len(new_email_domain_extension) < 1 or len(new_email_domain_extension) > 3:
                return 1
            if not new_email_domain_extension.isalpha():
                return 1

    return 0


def valid_parsing_emails():
    new_email_name = ''
    new_email_domain = ''
    number_of_str = int(input().lstrip().rstrip())
    for _ in range(number_of_str):
        source_s = input().lstrip().rstrip()
        new_name, new_email = email.utils.parseaddr(source_s)
        match = re.search(r'[@]', new_email)
        if not match:
            continue
        new_email_name = new_email[:match.start()]
        if valid_email_name(new_email_name) != 0:
            # print(new_email_name)
            # print('{} is not valid'.format(email.utils.formataddr((new_name, new_email))))
            continue
        else:
            if valid_email_domain(new_email_name, source_s) != 0:
                continue
            else:
                print(email.utils.formataddr((new_name, new_email)))


# TODO 10: "Validating UID"
def check_3digits(uid):
    match = re.findall(r'\d', uid)
    # print(match, len(match))
    if len(match) < 3:
        return False
    else:
        return True


def check_only_10_alphanumeric(uid):
    if uid.lower().isalnum() and len(uid) == 10:
        return True
    else:
        return False


def no_repeat(uid):
    for ch in uid:
        match = re.findall(ch, uid)
        # print(match, len(match))
        if len(match) != 1:
            return False
        else:
            continue
    return True


def check_2uppercase_english(uid):
    count = 0
    for ch in uid:
        if ch in 'QWRTYPSDFGHJKLZXCVBNMAEIOU':
            count += 1
        else:
            continue
    if count < 2:
        return False
    else:
        return True


def valid_uid():
    number_of_str = int(input().lstrip().rstrip())
    my_uid = Uid(number_of_str)
    my_uid.check_valid_uid()
    # for _ in range(number_of_str):
    #     uid = input().lstrip().rstrip()
    #     if check_only_10_alphanumeric(uid) and check_3digits(uid) and no_repeat(uid) and check_2uppercase_english(uid):
    #         print('Valid')
    #     else:
    #         print('Invalid')


class Uid():
    uid = None

    def __init__(self, inp):
        self.uid = inp

    def check_valid(self):
        if check_only_10_alphanumeric(self.uid) and check_3digits(self.uid) and no_repeat(
                self.uid) and check_2uppercase_english(self.uid):
            return True
        else:
            return False


# TODO 11: "Validating Credit Card Numbers"
class CreditCard():
    number = ''

    def __init__(self, inp):
        self.number = inp
        if not self.is_only_digits():
            print('Invalid')
        elif not self.check_first_digits():
            print('Invalid')
        elif not self.four_or_less_repeat():
            print('Invalid')
        else:
            print('Valid')

    def check_first_digits(self):
        if self.number[0] == '4' or self.number[0] == '5' or self.number[0] == '6':
            return True
        else:
            return False

    def four_or_less_repeat(self):
        test_str = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999']
        for test_dig in test_str:
            match = re.findall(test_dig, self.number)
            if len(match):
                return False
            else:
                continue
        return True

    def is_only_digits(self):
        match = ''.join(re.findall(r'[^\d]', self.number))
        if self.number.isdigit() and len(self.number) == 16:
            return True
        if len(match) != 3:
            return False
        match = ''.join(re.findall(r'[^-]', match))
        if len(match):
            print('More ---')
            return False
        groups = self.number.split('-')
        if len(groups) != 4:
            return False
        for i in groups:
            if len(i) != 4:
                return False
        match = ''.join(re.findall(r'[\d]', self.number))
        if match.isdigit() and len(match) == 16:
            self.number = match
            return True
        else:
            return False


# TODO 12: "Validating Postal Codes"
def check_post_code(post_code):
    match = ''.join(re.findall(r'[^\d]', post_code))
    is_digit = not bool(len(match))
    try:
        chek_size = not bool(len(list(filter(lambda x: x > 999999 or x < 100000, [int(post_code)]))))
    except ValueError:
        return False
    # print(chek_size)
    count_alternating_repetitive_digit = 0
    left_list = [post_code[i] for i in range(0, 6, 2)]
    right_list = [post_code[i] for i in range(1, 6, 2)]
    left_str = ''.join(left_list)
    right_str = ''.join(right_list)
    left_list = list(map(lambda x: re.findall(x + x, left_str), [x for x in set(left_list)]))

    count_alternating_repetitive_digit += reduce(lambda x, y: x + y, [len(x) for x in left_list])
    # print(count_alternating_repetitive_digit)
    right_list = list(map(lambda x: re.findall(x + x, right_str), [x for x in set(right_list)]))
    count_alternating_repetitive_digit += reduce(lambda x, y: x + y, [len(x) for x in right_list])
    check_alternating_repetitive_digit = not [x > 1 for x in [count_alternating_repetitive_digit]][0]
    return chek_size and check_alternating_repetitive_digit and is_digit


def main():
    # introduction_to_regex()
    # valid_roman_numerals()
    # valid_phone_numbers()
    # valid_parsing_emails()

    # number_of_str = int(input().lstrip().rstrip())
    # for _ in range(number_of_str):
    #     my_uid = Uid(input().lstrip().rstrip())
    #     if my_uid.check_valid():
    #         print('Valid')
    #     else:
    #         print('Invalid')

    # number_of_str = int(input().lstrip().rstrip())
    # for _ in range(number_of_str):
    #     my_card = CreditCard(input().lstrip().rstrip())

    post_code_str = int(input().lstrip().rstrip())
    print(check_post_code(post_code_str))


if __name__ == '__main__':
    main()
