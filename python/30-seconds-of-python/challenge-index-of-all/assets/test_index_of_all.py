import unittest
import sys

sys.path.append("/home/labex/project")
from index_of_all import *


def index_of_all(lst, value):
    return [i for i, x in enumerate(lst) if x == value]


class TestIndexOfAll(unittest.TestCase):
    def test_index_of_all(self):
        self.assertEqual(index_of_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), [4])
        self.assertEqual(index_of_all([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10], 5), [4, 5])
        self.assertEqual(index_of_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), [])
        self.assertEqual(index_of_all([], 5), [])


if __name__ == "__main__":
    unittest.main()
