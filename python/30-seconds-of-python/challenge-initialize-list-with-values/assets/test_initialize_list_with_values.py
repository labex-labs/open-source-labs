import unittest
import sys

sys.path.append("/home/labex/project")
from initialize_list_with_values import *


def initialize_list_with_values(n, val=0):
    return [val for x in range(n)]


class TestInitializeListWithValues(unittest.TestCase):
    def test_with_zero_value(self):
        self.assertEqual(initialize_list_with_values(5), [0, 0, 0, 0, 0])

    def test_with_non_zero_value(self):
        self.assertEqual(initialize_list_with_values(3, 2), [2, 2, 2])

    def test_with_negative_value(self):
        self.assertEqual(initialize_list_with_values(-2, 3), [])


if __name__ == "__main__":
    unittest.main()
