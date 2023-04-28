import unittest
import sys

sys.path.append("/home/labex/project")
from includes_all import *


class TestIncludesAll(unittest.TestCase):
    def test_includes_all(self):
        self.assertTrue(includes_all([1, 2, 3, 4, 5], [1, 3, 5]))
        self.assertFalse(includes_all([1, 2, 3, 4, 5], [1, 3, 6]))
        self.assertTrue(includes_all(["a", "b", "c"], ["a", "c"]))
        self.assertFalse(includes_all(["a", "b", "c"], ["a", "d"]))
        self.assertTrue(includes_all([], []))
        self.assertFalse(includes_all([], [1, 2, 3]))


if __name__ == "__main__":
    unittest.main()