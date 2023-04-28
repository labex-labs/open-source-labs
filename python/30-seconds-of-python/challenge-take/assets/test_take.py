import unittest
import sys

sys.path.append("/home/labex/project")
from take import *


class TestTake(unittest.TestCase):
    def test_take_default(self):
        self.assertEqual(take([1, 2, 3]), [1])

    def test_take_custom(self):
        self.assertEqual(take([1, 2, 3], 2), [1, 2])

    def test_take_empty(self):
        self.assertEqual(take([]), [])

    def test_take_string(self):
        self.assertEqual(take("hello"), "h")

    def test_take_string_custom(self):
        self.assertEqual(take("hello", 3), "hel")


if __name__ == "__main__":
    unittest.main()
