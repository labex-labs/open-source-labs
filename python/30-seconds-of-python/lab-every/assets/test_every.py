import unittest
import sys

sys.path.append("/home/labex/project")
from every import *


def every(lst, fn=lambda x: x):
    return all(map(fn, lst))


class TestEvery(unittest.TestCase):
    def test_all_true(self):
        self.assertTrue(every([2, 4, 6, 8], lambda x: x % 2 == 0))

    def test_all_false(self):
        self.assertFalse(every([1, 3, 5, 7], lambda x: x % 2 == 0))

    def test_mixed(self):
        self.assertFalse(every([2, 4, 5, 8], lambda x: x % 2 == 0))

    def test_empty_list(self):
        self.assertTrue(every([]))

    def test_default_fn(self):
        self.assertTrue(every([True, True, True]))
        self.assertFalse(every([True, False, True]))


if __name__ == "__main__":
    unittest.main()
