''' Python question by HackerRank
TODO 1: "XML 1 - Find the Score"
you are given a valid XML document, and you have to print its score. The score is calculated by the sum of
the score of each element. For any element, the score is equal to the number of attributes it has.
Input Format:
The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.
Output Format:
Output a single line, the integer score of the given XML document.
he feed and subtitle tag have one attribute each - lang.
The title and updated tags have no attributes.
The link tag has three attributes - rel, type and href.
So, the total score is 1+1+3=5.
There may be any level of nesting in the XML document. To learn about XML parsing, refer here.

'''

from fractions import Fraction
from functools import reduce
import re
import sys


# import xml.etree.cElementTree as etree
# from xml.etree import ElementTree as etree


# TODO 1: "XML 1 - Find the Score"
def xml_1_find_the_score():
    number_of_attributes = 0
    number_of_line = int(input().lstrip().rstrip())
    for _ in range(number_of_line):
        xml_line = input().lstrip().rstrip()
        pattern = re.compile(r'\w+=\'\w+')
        attribute_list = pattern.findall(xml_line)
        # tree = etree.ElementTree(etree.fromstring(xml_line))
        number_of_attributes += len(attribute_list)
    print(number_of_attributes)


def main():
    xml_1_find_the_score()


if __name__ == '__main__':
    main()
