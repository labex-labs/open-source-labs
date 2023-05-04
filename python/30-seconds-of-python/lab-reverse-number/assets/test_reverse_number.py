import unittest
import sys

sys.path.append("/home/labex/project")
from reverse_number import *
from math import copysign


class TestReverseNumber(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(reverse_number(123), 321)

    def test_negative_number(self):
        self.assertEqual(reverse_number(-456), -654)

    def test_zero(self):
        self.assertEqual(reverse_number(0), 0)

    def test_decimal_number(self):
        self.assertEqual(reverse_number(12.34), 43.21)

    def test_large_number(self):
        self.assertEqual(reverse_number(123456789), 987654321)


if __name__ == "__main__":
    unittest.main()
