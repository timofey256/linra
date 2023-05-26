import sys
sys.path.append('../linra')

from src.matrix import Matrix
import unittest

class TestMatrix(unittest.TestCase):

    def test_add(self):
        a = Matrix([[1, 2, 3], [10, -12, 7], [0, 2, -4]])
        b = Matrix([[5, 9, 7], [-8, 4, 9], [10, 4, 3]])
        res = Matrix([[5, 11, 10], [2, -8, 16], [10, 6, -1]])
        self.assertEqual((a+b), res)

if __name__ == "__main__":
    unittest.main()
