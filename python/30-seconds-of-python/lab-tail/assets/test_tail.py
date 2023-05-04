import unittest
import sys

sys.path.append("/home/labex/project")
from tail import *


class TestTail(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(tail([]), [])

    def test_single_element_list(self):
        self.assertEqual(tail([1]), [1])

    def test_multiple_element_list(self):
        self.assertEqual(tail([1, 2, 3]), [2, 3])

    def test_list_with_none(self):
        self.assertEqual(tail([None, 1, 2]), [1, 2])

    def test_list_with_strings(self):
        self.assertEqual(tail(["a", "b", "c"]), ["b", "c"])


if __name__ == "__main__":
    unittest.main()
