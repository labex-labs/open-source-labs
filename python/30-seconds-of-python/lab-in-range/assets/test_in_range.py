import unittest
import sys

sys.path.append("/home/labex/project")
from in_range import *


class TestInRange(unittest.TestCase):
    def test_in_range(self):
        self.assertTrue(in_range(5, 1, 10))
        self.assertTrue(in_range(3, 3, 3))
        self.assertTrue(in_range(-2, -5, 0))
        self.assertTrue(in_range(-2, 0, -5))
        self.assertFalse(in_range(10, 1, 5))


if __name__ == "__main__":
    unittest.main()
