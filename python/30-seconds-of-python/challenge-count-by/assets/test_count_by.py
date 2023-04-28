import unittest
import sys

sys.path.append("/home/labex/project")
from count_by import *
from collections import defaultdict
from math import floor

def count_by(lst, fn = lambda x: x):
  count = defaultdict(int)
  for val in map(fn, lst):
    count[val] += 1
  return dict(count)

class TestCountBy(unittest.TestCase):
    def test_count_by_floor(self):
        self.assertEqual(count_by([6.1, 4.2, 6.3], floor), {6: 2, 4: 1})

    def test_count_by_len(self):
        self.assertEqual(count_by(['one', 'two', 'three'], len), {3: 2, 5: 1})

if __name__ == '__main__':
    unittest.main()