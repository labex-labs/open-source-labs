import unittest
import sys

sys.path.append("/home/labex/project")
from min_by import *


class TestMinBy(unittest.TestCase):
    def test_min_by(self):
        lst = [1, 2, 3, 4, 5]
        fn = lambda x: x * 2
        self.assertEqual(min_by(lst, fn), 2)

        lst = ["apple", "banana", "cherry", "date"]
        fn = lambda x: len(x)
        self.assertEqual(min_by(lst, fn), "date")

        lst = [(1, 2), (3, 4), (5, 6)]
        fn = lambda x: x[1]
        self.assertEqual(min_by(lst, fn), (1, 2))


if __name__ == "__main__":
    unittest.main()