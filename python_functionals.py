''' Python question by HackerRank
TODO 1:
"Validating Email Addresses With a Filter"
You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.
Valid email addresses must follow these rules:
It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is 3.
Input Format
The first line of input is the integer N, the number of email addresses.
N lines follow, each containing a string.
Constraints: Each line is a non-empty string.
Output Format:
Output a list containing the valid email addresses in lexicographical order. If the list is empty, just output an empty list, [].

# TODO 2: "Reduce Function"
Given a list of rational numbers,find their product.
Input Format:
First line contains N, the number of rational numbers.
The i_th of next N lines contain two integers each, the numerator(N_i ) and denominator( D_i ) of the  rational number in the list.
Constraints: 1 <= N <= 100
1 <= N_i,D_i <= 10**9
Output Format
Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest
form, i.e. numerator and denominator have no common divisor other than 1.

# TODO 3: "Matrix Script"
Neo has a complex matrix script. The matrix script is a N x M grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.
If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.
Neo feels that there is no need to use 'if' conditions for decoding.
Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
Input Format
The first line contains space-separated integers N (rows) and M (columns) respectively.
The next N lines contain the row elements of the matrix script.
Constraints: 0 < N,M < 100
Note: A 0 score will be awarded for using 'if' conditions in your code.
Output Format
Print the decoded matrix script.

'''


from fractions import Fraction
from functools import reduce
import re


# TODO 1: "Validating Email Addresses With a Filter"
def test_email_consist(s):
    if s.count('@') == 1 and s.find('@') > 1 and s.find('@') < s.find('.') and s.find('.') < len(s) - 1 and s.find(
            '.') > len(s) - 5:
        return True
    else:
        return False


def test_email_user_name(s):
    user_name = s[:s.find('@')]
    test_s = list(filter(lambda x: not (x.isalnum() or x == '-' or x == '_'), user_name))
    if test_s:
        return False
    else:
        return True


def test_email_host_name(s):
    host_name = s[s.find('@') + 1:s.find('.')]
    # print(host_name)
    test_s = list(filter(lambda x: not x.isalnum(), host_name))
    # print(test_s)
    if test_s:
        return False
    else:
        return True


def fun(s):
    if not test_email_consist(s):
        return False
    if not test_email_user_name(s):
        return False
    if not test_email_host_name(s):
        return False
    return True


def filter_mail(emails):
    return list(filter(fun, emails))


# TODO 2: "Reduce Function"
def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)  # complete this line with a reduce statement, [1 2], [3 4], [10 6]
    # a = Fraction(*[int(x) for x in input().lstrip().rstrip().split()])
    # b = Fraction(*[int(x) for x in input().lstrip().rstrip().split()])
    # c = a*b
    # print(c.numerator, c.denominator)
    return t.numerator, t.denominator


# TODO 3: "Matrix Script"
def list_to_row_column_and_reverse(source_list, row, column):
    new_matrix = []
    # for i in (range(0, column)):
    #     new_matrix.append(source_list[i::column])
    new_matrix = [source_list[x::column] for x in [i for i in range(0, column)]]
    return new_matrix


def matrix_to_string(matrix):
    # new_string = ''.join([''.join(x) for x in matrix])
    new_list = [''.join(x) for x in matrix]
    new_string = ''.join(new_list)
    return new_string


def matrix_script():
    matrix = []
    result_string = ''
    number_of_row, number_of_column = list(map(int, input().split()))
    # print('number_of_column =', number_of_column, ',', 'number_of_row =', number_of_row)
    for i in range(number_of_row):
        row = [x for x in input()]
        for v in row[:number_of_column]:
            matrix.append(v)
    # matrix = list_to_row_column_and_reverse(matrix, number_of_row, number_of_column)
    matrix = [matrix[x::number_of_column] for x in [i for i in range(0, number_of_column)]]
    # unfiltered_string = matrix_to_string(matrix)
    new_list = [''.join(x) for x in matrix]
    unfiltered_string = ''.join(new_list)
    alnum_list = list(filter(lambda x: x.isalnum(), [x for x in unfiltered_string]))
    try:
        first_alnum = alnum_list[0]
    except IndexError:
        result_string = unfiltered_string
    else:
        last_alnum_index = unfiltered_string.rfind(alnum_list.pop())
        first_alnum_index = unfiltered_string.find(first_alnum)
        template_i = ['$', '#', '%', '!', '@', '&', '   ', '  ']  # !,@,#,$,%,&
        template_for_reduce = list(zip(template_i, [' '] * len(template_i)))
        result_string = unfiltered_string[first_alnum_index:last_alnum_index + 1:]
        result_string = reduce(lambda x, y: x.replace(*y), template_for_reduce, result_string)
        result_string = unfiltered_string[:first_alnum_index] + result_string + unfiltered_string[
                                                                                last_alnum_index + 1::]
    finally:
        print(result_string)


def fibonacci(n):
    # return a list of fibonacci numbers
    new_list = []
    if n == 0:
        return new_list
    new_list.append(0)
    if n == 1:
        return new_list
    new_list.append(1)
    if n == 2:
        return new_list
    for _ in range(n - 2):
        k1 = new_list.pop()
        k2 = new_list.pop()
        new_list.append(k2)
        new_list.append(k1)
        new_list.append(k1 + k2)
    return new_list


def main():
    # matrix_script()
    cube = list(map(lambda x: x ** 3, fibonacci(int(input()))))  # complete the lambda function
    print(cube)

if __name__ == '__main__':
    main()
