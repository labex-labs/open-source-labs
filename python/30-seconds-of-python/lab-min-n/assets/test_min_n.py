import unittest
import sys

sys.path.append("/home/labex/project")
from min_n import *


class TestMinN(unittest.TestCase):
    def test_min_n(self):
        self.assertEqual(min_n([1, 2, 3, 4, 5]), [1])
        self.assertEqual(min_n([5, 4, 3, 2, 1], 3), [1, 2, 3])
        self.assertEqual(min_n([1, 1, 1, 1, 1], 2), [1, 1])
        self.assertEqual(min_n([1]), [1])
        self.assertEqual(min_n([]), [])


if __name__ == "__main__":
    unittest.main()
