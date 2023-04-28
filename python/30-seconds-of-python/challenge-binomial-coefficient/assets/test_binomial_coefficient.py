import unittest
import sys

sys.path.append("/home/labex/project")
from binomial_coefficient import *
from math import comb


class TestBinomialCoefficient(unittest.TestCase):
    def test_binomial_coefficient(self):
        self.assertEqual(binomial_coefficient(5, 2), 10)
        self.assertEqual(binomial_coefficient(10, 5), 252)
        self.assertEqual(binomial_coefficient(0, 0), 1)
        self.assertEqual(binomial_coefficient(1, 0), 1)
        self.assertEqual(binomial_coefficient(1, 1), 1)
        self.assertEqual(binomial_coefficient(100, 50), 100891344545564193334812497256)


if __name__ == "__main__":
    unittest.main()
