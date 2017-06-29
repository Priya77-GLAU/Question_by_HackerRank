''' Python question by HackerRank
TODO 1:
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width W.
Input Format
The first line contains a string, S.
The second line contains the width, W.
Constraints:  0 < len(s) < 1000;  0 < w < len(s)
Output Format: Print the text wrapped paragraph.
TODO 2:
You are given a string S. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format: A single line containing a string .
Constraints: 0 < Len(S) <= 1000
Output Format: Print the modified string .
Sample Input: HackerRank.com presents "Pythonist 2".
TODO 3:
String Split and Join
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
Input Format: The first line contains a string consisting of space separated words.
Output Format: Print the formatted string as explained above.
TODO 4:
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
TODO 5:
Given an integer, N, print the following values for each integer  from  to :
Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each  from  to . Each value should be
space-padded to match the width of the binary value of .
Input Format: A single integer denoting N.
Constraints: 1 <= N <= 99
Output Format: Print N lines where each line  (in the range 1 <= i <= N) contains the respective decimal, octal,
capitalized hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.
TODO 6:
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
TODO 7:
You are given a string S. Your task is to capitalize each word of S.
Input Format: A single line of input containing the string, S.
Constraints:  0 < len(s) < 1000
The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
Output Format: Print the capitalized string, S.
'''

import textwrap
import string

#############################################################################################################
#TODO 1:
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

#############################################################################################################
#TODO 2:
def swap_case(s):
    new_str = ''
    for si in s:
        if si.islower():
            new_str += si.upper()
        elif si.isupper():
            new_str += si.lower()
        else:
            new_str += si
    return new_str

#############################################################################################################
#TODO 3:
def split_and_join(line):
    # write your code here
    new_line = line.split(' ')
    return str('-'.join(new_line))

#############################################################################################################
#TODO 4:
# def main():
#     N = 7
#     M = 21
#     for i in range(1, N, 2):
#         print(('.|.'*i).center(M,'-'))
#     print(('WELCOME').center(M,'-'))
#     for i in range(N - 2, -1, -2):
#         print(('.|.'*i).center(M,'-'))

#############################################################################################################
#TODO 5: String Formatting
def print_formatted(number):
    # your code goes here
    num_s = bin(number)[2:]
    width = len(num_s)
    for it_number in range(1,number+1):
        num_s = ''
        num_s = str(it_number).rjust(width) + ' ' + oct(it_number)[2:].rjust(width) + ' ' + hex(it_number)[2:].upper().rjust(width) + ' ' + bin(it_number)[2:].rjust(width)
        print(num_s)
    num_s = num_s.rjust(width)
    return num_s

#############################################################################################################
#TODO 6: Alphabet Rangoli
def str_rangoli(string):
    if len(string) == 1:
        return string
    else:
        return string[0] + '-' + str_rangoli(string[1:])+ '-' + string[0]


def print_rangoli(size):
    # your code goes here
    alph_str = string.ascii_lowercase[size-1::-1]
    width = (size*2-1)*2-1
    for i in range(len(alph_str)):
        print(str_rangoli(alph_str[:i+1]).center(width,'-'))

    alph_str = alph_str[:-1]
    for i in range(len(alph_str[1:]),-1,-1):
        print(str_rangoli(alph_str[:i+1]).center(width,'-'))


#TODO 6.1: Alphabet Rangoli - other way
def print_rangoli_new(size):
    alph_str = string.ascii_lowercase[size - 1::-1]
    width = (size * 2 - 1) * 2 - 1
    k = 1
    i = 1
    while i > 0:
        print(str_rangoli(alph_str[:i]).center(width, '-'))
        i += k
        if i == (size):
            k = -k

# TODO 7: "Capitalize!"
def capitalize(string):
    new_string = ''
    i = 0
    for s in string:
        if s == ' ':
            new_string = new_string + s
            i = 0
        elif i == 0:
            new_string = new_string + s.upper()
            i += 1
        else:
            new_string = new_string + s
            i += 1
    return new_string
#############################################################################################################
def main():
    # print_rangoli(5)
    # print_rangoli_new(5)
    test_string = 'hello woRld from my 100s hearts'
    # test_string = 'q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'
    print(capitalize(test_string))

#############################################################################################################
if __name__ == '__main__':
    main()
