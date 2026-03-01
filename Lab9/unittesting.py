import unittest
from Calculation import *


def addtwonumbers(a, b):
    return a + b


class TestAddFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(addtwonumbers(1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(subtracttwonumbers(6, 4), 2)
        self.assertEqual(subtracttwonumbers(4, 6), -2)

    def test_multiplication(self):
        self.assertEqual(multiplythreenumbers(1, 2, 3), 6)
        self.assertEqual(multiplythreenumbers(1, -2, 3), -6)
        self.assertEqual(multiplythreenumbers(1, -2, -3), 6)
        self.assertEqual(multiplythreenumbers(-1, -2, -3), -6)

    def test_division(self):
        self.assertEqual(dividetwonnumbers(6, 3), 2)
        self.assertAlmostEqual(dividetwonnumbers(10, 3), 3.3333333, places=7)

    # unit test for division by zero
    def test_division_by_zero(self):
        self.assertIsNone(dividetwonnumbers(10, 0))

    # unit test for value error
    def test_division_with_string(self):
        self.assertIsNone(dividetwonnumbers(10, "a"))
        self.assertIsNone(dividetwonnumbers("Peter", 2))

    # unit test for unexpected exception
    def test_unexpected_exception(self):
        with self.assertRaises(TypeError):
         # Passing no values to function
            dividetwonnumbers()   
if __name__ == '__main__':
    unittest.main()