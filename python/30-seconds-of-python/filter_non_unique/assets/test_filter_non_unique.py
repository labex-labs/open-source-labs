import unittest
import sys
sys.path.append("/home/labex/project")
from filter_non_unique import *
from collections import Counter

def filter_non_unique(lst):
  return [item for item, count in Counter(lst).items() if count == 1]

class TestFilterNonUnique(unittest.TestCase):
  
  def test_filter_non_unique(self):
    self.assertEqual(filter_non_unique([1, 2, 3, 3, 4, 5, 5]), [1, 2, 4])
    self.assertEqual(filter_non_unique(['a', 'b', 'c', 'c', 'd', 'e', 'e']), ['a', 'b', 'd'])
    self.assertEqual(filter_non_unique([True, False, True, False, True]), [])
    self.assertEqual(filter_non_unique([]), [])
    
if __name__ == '__main__':
  unittest.main()