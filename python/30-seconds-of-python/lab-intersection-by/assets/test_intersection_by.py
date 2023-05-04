import unittest
import sys

sys.path.append("/home/labex/project")
from intersection_by import *


from math import floor


def intersection_by(a, b, fn):
    _b = set(map(fn, b))
    return [item for item in a if fn(item) in _b]


class TestIntersectionBy(unittest.TestCase):
    def test_intersection_by_floor(self):
        self.assertEqual(intersection_by([2.1, 1.2], [2.3, 3.4], floor), [2.1])


if __name__ == "__main__":
    unittest.main()
