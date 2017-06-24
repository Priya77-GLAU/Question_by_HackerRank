''' Python question by HackerRank
TODO 1: What's Your Name
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
Hello firstname lastname! You just delved into python.
Input Format: The first line contains the first name, and the second line contains the last name.
Constraints: The length of the first and last name ≤ 10.
Output Format: Print the output as mentioned above.
Sample Input
Guido
Rossum
Sample Output
Hello Guido Rossum! You just delved into python.
Explanation
The input read by the program is stored as a string data type. A string is a collection of characters.
TODO 2: Mutations
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
Let's try to understand this with an example.
You are given an immutable string, and you want to make changes to it.
Example
string = "abracadabra"
You can access an index by:
print string[5]
a
What if you would like to assign a value?
string[5] = 'k'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
How would you approach this?
One solution is to convert the string to a list and then change the value.
Example
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print string
abrackdabra
Another approach is to slice the string and join it back.
Example
string = string[:5] + "k" + string[6:]
print string
abrackdabra
Task
Read a given string, change the character at a given index and then print the modified string.
Input Format
The first line contains a string, .
The next line contains an integer , denoting the index location and a character  separated by a space.
Output Format
Using any of the methods explained above, replace the character at index  with character .
TODO 3: Find a string
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.
Input Format
The first line of input contains the original string. The next line contains the substring.
Constraints
1 <= len(string) <=200
Each character in the string is an ascii character.
Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.
Sample Input
ABCDCDC
CDC
Sample Output
2
Concept
Some string processing examples, such as these, might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where  is the string.
To traverse through the length of a string, use a for loop:
for i in range(0, len(s)):
    print (s[i])
A range function is used to loop over some length:
range (0, 5)
Here, the range loops over 0 to 4.  5 is excluded.
TODO 4:
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
Input Format
A single line containing a string S.
Constraints 0 < len(S) < 1000
Output Format
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
Sample Input
qA2
Sample Output
True
True
True
True
True
TODO 5:
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.
Input Format
A single line containing the thickness value for the logo.
Constraints
The thickness must be an odd number.
0 <= thickness <= 50
Output Format:  Output the desired logo.
'''

from functools import *

#############################################################################################################
#TODO 1:
def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))
#############################################################################################################
#TODO 2:
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

#############################################################################################################
#TODO 3:
def count_substring(string, sub_string):
    count=0
    start=0
    while True:
        n=string.find(sub_string, start)
        if n == -1:
            break
        else:
            count+=1
            start=n+1
    return count
#############################################################################################################
#TODO 4:
s='qA2'
#
# m=list(map(str.isalnum ,[i for i in s]))
# print(reduce(lambda x,y: x or y,m))
#
# m=list(map(str.isalpha ,[i for i in s]))
# print(reduce(lambda x,y: x or y,m))
#
# m=list(map(str.isdigit ,[i for i in s]))
# print(reduce(lambda x,y: x or y,m))
#
# m=list(map(str.islower ,[i for i in s]))
# print(reduce(lambda x,y: x or y,m))
#
# m=list(map(str.isupper ,[i for i in s]))
# print(reduce(lambda x,y: x or y,m))

#############################################################################################################
#TODO 5:

#############################################################################################################

# def main():


#############################################################################################################
# main()

thickness = int(input()) #This must be an odd number
# thickness = 5
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

