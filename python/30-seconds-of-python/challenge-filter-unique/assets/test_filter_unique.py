import unittest
import sys

sys.path.append("/home/labex/project")
from filter_unique import *
from collections import Counter


def filter_unique(lst):
    return [item for item, count in Counter(lst).items() if count > 1]


class TestFilterUnique(unittest.TestCase):
    def test_filter_unique(self):
        self.assertEqual(filter_unique([1, 2, 3, 4, 5]), [])
        self.assertEqual(filter_unique([1, 2, 2, 3, 4, 4, 5]), [2, 4])
        self.assertEqual(filter_unique(["a", "b", "c", "c", "d", "d", "d"]), ["c", "d"])
        self.assertEqual(filter_unique([]), [])
