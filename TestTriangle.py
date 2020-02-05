# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidInputs(self):
        self.assertNotEqual(classifyTriangle(300, 300, 300), 'Equilateral',
                            '300, 300, 300 is invalid input and not "Equilateral"')
        self.assertNotEqual(classifyTriangle(-3, -4, -5), 'Right', '-3, -4, -5 is invalid input and not "Right"')
        self.assertNotEqual(classifyTriangle("2", 2, 2), 'Equilateral', '"2" is a string and invalid input')
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1, 2, 3 is not a triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral', '2, 2, 2 is a Equilateral triangle')
        self.assertNotEqual(classifyTriangle(3, 4, 5), 'Equilateral', '4, 4, 5 is not a Equilateral triangle')

    def testRightTriangles(self):
        self.assertEqual(classifyTriangle(5, 4, 3), 'Right', '5, 4, 3 is a Right triangle')
        self.assertNotEqual(classifyTriangle(4, 4, 5), 'Right', '4, 4, 5 is not a Right triangle')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5, 6, 7), 'Scalene', '5, 6, 7 is Scalene')
        self.assertNotEqual(classifyTriangle(4, 4, 5), 'Scalene', '4, 4, 5 is not a Scalene triangle')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(5, 5, 7), 'Isoceles', '5, 6, 7 is Isoceles')
        self.assertNotEqual(classifyTriangle(3, 4, 5), 'Isoceles', '4, 4, 5 is not a Isoceles triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
