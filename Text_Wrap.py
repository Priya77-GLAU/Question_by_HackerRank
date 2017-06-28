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
TODO 2:
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
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

#############################################################################################################
def main():
    N = 7
    M = 21
    for i in range(1, N, 2):
        print(('.|.'*i).center(M,'-'))
    print(('WELCOME').center(M,'-'))
    for i in range(N - 2, -1, -2):
        print(('.|.'*i).center(M,'-'))

#############################################################################################################
if __name__ == '__main__':
    main()
