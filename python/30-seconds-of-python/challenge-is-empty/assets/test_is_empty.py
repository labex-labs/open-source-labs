import unittest
import sys

sys.path.append("/home/labex/project")
from is_empty import *


class TestIsEmpty(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_empty(""))

    def test_non_empty_string(self):
        self.assertFalse(is_empty("hello"))

    def test_empty_list(self):
        self.assertTrue(is_empty([]))

    def test_non_empty_list(self):
        self.assertFalse(is_empty([1, 2, 3]))

    def test_empty_dict(self):
        self.assertTrue(is_empty({}))

    def test_non_empty_dict(self):
        self.assertFalse(is_empty({"key": "value"}))

    def test_zero(self):
        self.assertTrue(is_empty(0))

    def test_non_zero(self):
        self.assertFalse(is_empty(42))


if __name__ == "__main__":
    unittest.main()
