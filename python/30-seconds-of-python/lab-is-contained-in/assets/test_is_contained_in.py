import unittest
import sys

sys.path.append("/home/labex/project")
from is_contained_in import *


class TestIsContainedIn(unittest.TestCase):
    def test_is_contained_in(self):
        self.assertTrue(is_contained_in([1, 2, 3], [1, 2, 3, 4, 5]))
        self.assertTrue(is_contained_in([1, 2, 3], [1, 1, 2, 2, 3, 3]))
        self.assertFalse(is_contained_in([1, 2, 3], [1, 2]))
        self.assertFalse(is_contained_in([1, 2, 3], [1, 1, 2, 2]))
        self.assertFalse(is_contained_in([1, 2, 3], [4, 5, 6]))


if __name__ == "__main__":
    unittest.main()
