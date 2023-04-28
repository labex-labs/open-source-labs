import unittest
import sys

sys.path.append("/home/labex/project")
from sort_by_indexes import *


class TestSortByIndexes(unittest.TestCase):
    def test_sort_by_indexes(self):
        lst = [4, 3, 2, 1]
        indexes = [3, 2, 1, 0]
        expected_output = [1, 2, 3, 4]
        self.assertEqual(sort_by_indexes(lst, indexes), expected_output)

        lst = ["a", "b", "c", "d"]
        indexes = [0, 2, 1, 3]
        expected_output = ["a", "c", "b", "d"]
        self.assertEqual(sort_by_indexes(lst, indexes), expected_output)

        lst = [10, 20, 30, 40]
        indexes = [0, 1, 2, 3]
        expected_output = [10, 20, 30, 40]
        self.assertEqual(sort_by_indexes(lst, indexes), expected_output)

        lst = ["apple", "banana", "cherry", "date"]
        indexes = [2, 0, 3, 1]
        expected_output = ["banana", "cherry", "date", "apple"]
        self.assertEqual(sort_by_indexes(lst, indexes), expected_output)


if __name__ == "__main__":
    unittest.main()