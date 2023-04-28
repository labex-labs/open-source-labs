import unittest
import sys

sys.path.append("/home/labex/project")
from median import *


class TestMedian(unittest.TestCase):
    def test_odd_list(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_even_list(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_duplicate_values(self):
        self.assertEqual(median([1, 2, 2, 3, 4]), 2)

    def test_negative_values(self):
        self.assertEqual(median([-1, -2, -3, -4, -5]), -3)

    def test_empty_list(self):
        self.assertRaises(IndexError, median, [])

    def test_single_value_list(self):
        self.assertEqual(median([5]), 5)


if __name__ == "__main__":
    unittest.main()
