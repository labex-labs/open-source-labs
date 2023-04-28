import unittest
import sys

sys.path.append("/home/labex/project")
from min_by import *


def min_by(lst, fn):
    return min(map(fn, lst))

class TestMinBy(unittest.TestCase):
    def test_min_by(self):
        self.assertEqual(min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v: v['n']), 2)

if __name__ == '__main__':
    unittest.main()