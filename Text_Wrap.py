''' Python question by HackerRank

You are given a string S and width W.
Your task is to wrap the string into a paragraph of width W.
Input Format
The first line contains a string, S.
The second line contains the width, W.
Constraints:  0 < len(s) < 1000;  0 < w < len(s)
Output Format: Print the text wrapped paragraph.

'''

import textwrap

#############################################################################################################
def wrap(string, max_width):
    s = textwrap.fill(string, max_width)
    print(s)
    return
#############################################################################################################
def main():
    wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)

#############################################################################################################
main()
