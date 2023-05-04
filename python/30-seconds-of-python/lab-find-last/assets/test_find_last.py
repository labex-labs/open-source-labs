import unittest
import sys

sys.path.append("/home/labex/project")
from find_last import *


def find_last(lst, fn):
    return next(x for x in lst[::-1] if fn(x))


class TestFindLast(unittest.TestCase):
    def test_find_last(self):
        lst = [1, 2, 3, 4, 5]
        fn = lambda x: x % 2 == 0
        self.assertEqual(find_last(lst, fn), 4)

        lst = ["apple", "banana", "cherry", "date"]
        fn = lambda x: x.startswith("c")
        self.assertEqual(find_last(lst, fn), "cherry")

        lst = [True, False, True, False]
        fn = lambda x: x
        self.assertEqual(find_last(lst, fn), True)


if __name__ == "__main__":
    unittest.main()
