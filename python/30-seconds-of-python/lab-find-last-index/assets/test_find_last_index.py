import unittest
import sys

sys.path.append("/home/labex/project")
from find_last_index import *


def find_last_index(lst, fn):
    return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))


class TestFindLastIndex(unittest.TestCase):
    def test_find_last_index(self):
        self.assertEqual(find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1), 2)


if __name__ == "__main__":
    unittest.main()
