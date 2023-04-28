import unittest
import sys

sys.path.append("/home/labex/project")
from bifurcate_by import *


def bifurcate_by(lst, fn):
    return [[x for x in lst if fn(x)], [x for x in lst if not fn(x)]]


class TestBifurcateBy(unittest.TestCase):
    def test_bifurcate_by(self):
        self.assertEqual(
            bifurcate_by([1, 2, 3, 4, 5], lambda x: x % 2 == 0), [[2, 4], [1, 3, 5]]
        )
        self.assertEqual(
            bifurcate_by(["apple", "banana", "cherry", "date"], lambda x: len(x) > 5),
            [["banana", "cherry"], ["apple", "date"]],
        )
        self.assertEqual(bifurcate_by([], lambda x: x > 0), [[], []])
        self.assertEqual(
            bifurcate_by([True, False, True], lambda x: x), [[True, True], [False]]
        )
        self.assertEqual(
            bifurcate_by([1, 2, 3, 4, 5], lambda x: x > 5), [[], [1, 2, 3, 4, 5]]
        )


if __name__ == "__main__":
    unittest.main()
