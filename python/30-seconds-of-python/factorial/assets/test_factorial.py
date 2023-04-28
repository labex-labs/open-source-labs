import unittest
import sys
sys.path.append("/home/labex/project")
from factorial import *

class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_negative(self):
        with self.assertRaises(Exception):
            factorial(-5)
    
    def test_factorial_float(self):
        with self.assertRaises(Exception):
            factorial(2.5)

if __name__ == '__main__':
    unittest.main()