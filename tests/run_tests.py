#!/usr/bin/env python3

import sys
sys.path.append('../linra')

from src.matrix import Matrix
from src.vector import Vector
from src.diagonalization import Diagonalization
from src.ortogonalization import Ortogonalization
import unittest

from operator import add, sub, mul

class TestData:
    a = Matrix([[1, 2, 3], [10, -12, 7], [0, 2, -4]])
    b = Matrix([[5, 9, 7], [-8, 4, 9], [10, 4, 3]])
    c = Matrix([[2,2], [4,1]])

    w = Matrix([[1,2,-1], [2,5,-3], [-1,-3,2]])
    v = Matrix([[1,0,1,0], [1,1,1,1], [1,0,0,1]])

    vectorW = Vector([2, 3, 5])
    vectorV = Vector([-2, 5, 9])
    vectorA = Vector([123123, -35231, 123])
    vectorB = Vector([-2434, 14, 12415])

class TestMatrix(unittest.TestCase):
    def runTestExceptionRaisingTemplate(self, op, data1=TestData.b, data2=TestData.c, exceptionType=ValueError):
        with self.assertRaises(exceptionType):
            op(data1, data2)
    
    def test_add(self):
        res = Matrix([[6, 11, 10], [2, -8, 16], [10, 6, -1]])
        self.assertEqual((TestData.a+TestData.b), res)

        self.runTestExceptionRaisingTemplate(add)
    
    def test_sub(self):
        res = Matrix([[-4, -7, -4], [18, -16, -2], [-10, -2, -7]])
        self.assertEqual((TestData.a-TestData.b), res)
        
        self.runTestExceptionRaisingTemplate(sub)

    def test_mul(self):
        res = Matrix([[19, 29, 34], [216, 70, -17], [-56, -8, 6]])
        self.assertEqual((TestData.a*TestData.b), res)

        self.runTestExceptionRaisingTemplate(mul)

    def test_transpose(self):
        res1 = Matrix([[2, 4], [2, 1]]) # Transpose of TestData.c
        res2 = Matrix([[1, 2, -1], [2, 5, -3], [-1, -3, 2]]) # Transpose of TestData.w

        self.assertEqual(TestData.c.transpose(), res1)
        #self.assertEqual(TestData.w.transpose(), res2)

    def test_standard_matrices(self):
        res1 = Matrix([[1,0,0], [0,1,0], [0,0,1]])
        res2 = Matrix([[0,0,0], [0,0,0], [0,0,0]])

        self.assertEqual(Matrix.create_unit_matrix(3,3), res1)
        self.assertEqual(Matrix.create_zero_matrix(3,3), res2)

class TestDiagonalization(unittest.TestCase):
    def testFormDiagonalization(self):
        res_form = Matrix([[1,0,0], [0,1,0], [0,0,0]])
        res_transition_matrix = Matrix([[1,-2,-1], [0,1,1],[0,0,1]])

        self.assertEqual(Diagonalization.diagonalize_form(TestData.w), (res_form, res_transition_matrix))

# class TestOrtogonalization(unittest.TestCase):
#     def testGramSchmidtOrtogonalization(self):
#         res = Matrix([[-0.6635, -0.3035, -0.4835, -0.4835], [0, 0, -0.7071, 0.7071], [0.5565, -0.8111, -0.1273, -0.1273]])

#         self.assertEqual(Ortogonalization.gram_schmidt(TestData.v), res)

class TestVector(unittest.TestCase):
    def testGeneral(self):
        with self.assertRaises(TypeError):
            TestData.vectorV + TestData.v
            TestData.v + TestData.vectorV
            TestData.vectorV + "asd"

    def testAddition(self):
        res = Vector([0, 8, 14])
        self.assertEqual(TestData.vectorV + TestData.vectorW, res)
        self.assertEqual(TestData.vectorW + TestData.vectorV, res)
        self.assertEqual(TestData.vectorA + TestData.vectorB, Vector([120689, -35217, 12538]))

    def testSubstitution(self):
        res = Vector([4, -2 ,-4])
        res_negation = Vector(list(map(lambda x: -x, res._data)))
        self.assertEqual(TestData.vectorW - TestData.vectorV, res)
        self.assertEqual(TestData.vectorV - TestData.vectorW, res_negation)

if __name__ == "__main__":
    unittest.main()