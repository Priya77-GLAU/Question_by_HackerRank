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


'''

from fractions import Fraction
from functools import reduce


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


def main():


if __name__ == '__main__':
    main()
