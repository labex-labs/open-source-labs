import unittest
import sys

sys.path.append("/home/labex/project")
from difference import *


class TestDifference(unittest.TestCase):
    def test_difference(self):
        self.assertEqual(difference([1, 2, 3], [2, 3, 4]), [1])
        self.assertEqual(difference([5, 6, 7], [7, 8, 9]), [5, 6])
        self.assertEqual(difference([10, 11, 12], [12, 13, 14]), [10, 11])
        self.assertEqual(difference([15, 16, 17], [16, 17, 18]), [15])
        self.assertEqual(difference([], [1, 2, 3]), [])
        self.assertEqual(difference([1, 2, 3], []), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
