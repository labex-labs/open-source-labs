import unittest
import sys

sys.path.append("/home/labex/project")
from transpose import *


def transpose(lst):
    return list(zip(*lst))


class TestTranspose(unittest.TestCase):
    def test_transpose(self):
        self.assertEqual(
            transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [(1, 4, 7), (2, 5, 8), (3, 6, 9)],
        )
        self.assertEqual(transpose([[1, 2], [3, 4], [5, 6]]), [(1, 3, 5), (2, 4, 6)])
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6]]), [(1, 4), (2, 5), (3, 6)])
        self.assertEqual(transpose([[1, 2], [3, 4]]), [(1, 3), (2, 4)])
        self.assertEqual(transpose([[1, 2, 3, 4]]), [(1,), (2,), (3,), (4,)])


if __name__ == "__main__":
    unittest.main()
