#!/bin/usr/env python3

import sys
sys.path.append('../linra')

from src.matrix import Matrix
import unittest

class TestData:
    a = Matrix([[1, 2, 3], [10, -12, 7], [0, 2, -4]])
    b = Matrix([[5, 9, 7], [-8, 4, 9], [10, 4, 3]])
    c = Matrix([[2,2], [4,1]])

class TestMatrix(unittest.TestCase):
    def test_add(self):
        res = Matrix([[6, 11, 10], [2, -8, 16], [10, 6, -1]])
        self.assertEqual((TestData.a+TestData.b), res)

        with self.assertRaises(ValueError):
            TestData.a+TestData.c
    
    def test_sub(self):
        res = Matrix([[-4, -7, -4], [18, -16, -2], [-10, -2, -7]])
        self.assertEqual((TestData.a-TestData.b), res)
        
        with self.assertRaises(ValueError):
            TestData.a-TestData.c

    def test_mul(self):
        res = Matrix([[19, 29, 34], [216, 70, -17], [-56, -8, 6]])
        self.assertEqual((TestData.a*TestData.b), res)

        with self.assertRaises(ValueError):
            TestData.a*TestData.c

if __name__ == "__main__":
    unittest.main()
