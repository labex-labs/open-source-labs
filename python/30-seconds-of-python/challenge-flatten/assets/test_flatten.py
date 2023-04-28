import unittest
import sys

sys.path.append("/home/labex/project")
from flatten import *


def flatten(lst):
    return [x for y in lst for x in y]


class TestFlatten(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(
            flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(flatten([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(flatten([[]]), [])
        self.assertEqual(flatten([[1, 2, 3, 4]]), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
