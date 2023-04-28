import unittest
import sys

sys.path.append("/home/labex/project")
from deep_flatten import *
from collections.abc import Iterable


def deep_flatten(lst):
    return (
        [a for i in lst for a in deep_flatten(i)]
        if isinstance(lst, Iterable)
        else [lst]
    )


class TestDeepFlatten(unittest.TestCase):
    def test_deep_flatten(self):
        self.assertEqual(deep_flatten([1, 2, [3, 4, [5, 6]]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(deep_flatten([1, [2, [3, [4, [5]]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(deep_flatten([1, [2, [3, [4, [5]]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(deep_flatten([1, [2, [3, [4, [5]]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(deep_flatten([1, [2, [3, [4, [5]]]]]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
