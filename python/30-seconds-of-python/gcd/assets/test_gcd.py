import unittest
from gcd import *
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)

class TestGcd(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd([10, 20, 30]), 10)
        self.assertEqual(gcd([15, 25, 35]), 5)
        self.assertEqual(gcd([18, 24, 36]), 6)
        self.assertEqual(gcd([7, 14, 21]), 7)
        self.assertEqual(gcd([100, 200, 300]), 100)

if __name__ == '__main__':
    unittest.main()