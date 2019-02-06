# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

import math

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInputA(self): 
        self.assertEqual(classifyTriangle(0,1,2),'InvalidInput','0,1,2 is a InvalidInput')

    def testInputB(self): 
        self.assertEqual(classifyTriangle(199,199,201),'InvalidInput','199,199,201 is a InvalidInput')

    def testInputC(self): 
        self.assertEqual(classifyTriangle(1.2, 2, 1.2),'InvalidInput','1.2, 2, 1.2 is a InvalidInput')

    def testInputD(self): 
        self.assertEqual(classifyTriangle(2,2,'three'),'InvalidInput','2,2, three is a InvalidInput')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(6,8,10),'Right','6,8,10 is a Right triangle')

    def testRightTriangleD(self): 
        self.assertEqual(classifyTriangle(10,8,6),'Right','10,8,6 is a Right triangle')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,2),'NotATriangle','1,1,2 is NotATriangle')

    def testIsoscelesTrianglesB(self): 
        self.assertEqual(classifyTriangle(10,10,11),'Isoceles','10,10,11 is a Isoceles triangle')

    def testScaleneTrianglesA(self): 
        self.assertEqual(classifyTriangle(10,12,11),'Scalene','10,12,11 is a Scalene triangle')

    def testScaleneTrianglesB(self): 
        self.assertEqual(classifyTriangle(10,12,32),'NotATriangle','10,12,32 is NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)

