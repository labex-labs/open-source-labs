import unittest
import sys

sys.path.append("/home/labex/project")
from initialize_list_with_range import *


def initialize_list_with_range(end, start=0, step=1):
    return list(range(start, end + 1, step))

class TestInitializeListWithRange(unittest.TestCase):
    def test_initialize_list_with_range_default(self):
        self.assertEqual(initialize_list_with_range(5), [0, 1, 2, 3, 4, 5])

    def test_initialize_list_with_range_start(self):
        self.assertEqual(initialize_list_with_range(7, 3), [3, 4, 5, 6, 7])

    def test_initialize_list_with_range_step(self):
        self.assertEqual(initialize_list_with_range(9, 0, 2), [0, 2, 4, 6, 8])

if __name__ == '__main__':
    unittest.main()