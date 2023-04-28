import unittest
import sys

sys.path.append("/home/labex/project")
from symmetric_difference_by import *


class TestSymmetricDifferenceBy(unittest.TestCase):
    def test_symmetric_difference_by(self):
        a = [1, 2, 3, 4]
        b = [3, 4, 5, 6]
        fn = lambda x: x % 2
        result = symmetric_difference_by(a, b, fn)
        self.assertEqual(result, [2, 5, 6])

        a = ["apple", "banana", "cherry"]
        b = ["orange", "banana", "kiwi"]
        fn = lambda x: len(x)
        result = symmetric_difference_by(a, b, fn)
        self.assertEqual(result, ["apple", "cherry", "orange", "kiwi"])


if __name__ == "__main__":
    unittest.main()