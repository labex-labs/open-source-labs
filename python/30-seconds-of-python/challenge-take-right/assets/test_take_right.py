import unittest
import sys

sys.path.append("/home/labex/project")
from take_right import *


class TestTakeRight(unittest.TestCase):
    def test_take_right_with_default_n(self):
        self.assertEqual(take_right([1, 2, 3, 4, 5]), [5])
        self.assertEqual(take_right("hello"), "o")

    def test_take_right_with_custom_n(self):
        self.assertEqual(take_right([1, 2, 3, 4, 5], 3), [3, 4, 5])
        self.assertEqual(take_right("hello", 2), "lo")

    def test_take_right_with_large_n(self):
        self.assertEqual(take_right([1, 2, 3, 4, 5], 10), [1, 2, 3, 4, 5])
        self.assertEqual(take_right("hello", 10), "hello")


if __name__ == "__main__":
    unittest.main()