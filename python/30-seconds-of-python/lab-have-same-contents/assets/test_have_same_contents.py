import unittest
import sys

sys.path.append("/home/labex/project")
from have_same_contents import *


class TestHaveSameContents(unittest.TestCase):
    def test_same_contents(self):
        self.assertTrue(have_same_contents([1, 2, 3], [3, 2, 1]))
        self.assertTrue(have_same_contents([1, 1, 2, 3], [3, 2, 1, 1]))
        self.assertTrue(have_same_contents([], []))

    def test_different_contents(self):
        self.assertFalse(have_same_contents([1, 2, 3], [4, 5, 6]))
        self.assertFalse(have_same_contents([1, 1, 2, 3], [3, 2, 1]))
        self.assertFalse(have_same_contents([1, 2, 3], [3, 2]))


if __name__ == "__main__":
    unittest.main()
