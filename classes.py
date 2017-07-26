''' Python question by HackerRank
TODO 1: "Class 2 - Find the Torsional Angle"
You are given four points A,B,C and D in a 3-dimensional Cartesian coordinate system. You are required to print the angle between the plane made by the points A,B,C and B,C,D in degrees(not radians). Let the angle be PHI.
Cos(phi) = (x.y)/|x||y|
 where x = AB*BC  and y = BC * CD .
Here,  x.y means the dot product of x and y, and AB*BC  means the cross product of vectors AB and BC. Also, AB = B - A.
Input Format:
One line of input containing the space separated floating number values of the X, Y  and Z coordinates of a point.
Output Format:
Output the angle correct up to two decimal places.

'''

import numpy
from fractions import Fraction
from functools import reduce
import re
import sys


# import xml.etree.cElementTree as etree
# from xml.etree import ElementTree as etree


# TODO 1: "Class 2 - Find the Torsional Angle"

class Points(object):
    x = float(0)
    y = float(0)
    z = float(0)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        new_point = Points(self.x - no.x, self.y - no.y, self.x - no.z)
        return new_point

    def dot(self, no):

    def cross(self, no):

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


def main():


if __name__ == '__main__':
    main()
