import unittest
import sys
sys.path.append("/home/labex/project")
from min_element_index import *


class TestMinElementIndex(unittest.TestCase):
  
  def test_min_element_index(self):
    self.assertEqual(min_element_index([3, 5, 1, 7, 2]), 2)
    self.assertEqual(min_element_index([0, 0, 0, 0, 0]), 0)
    self.assertEqual(min_element_index([-5, -2, -10, -8]), 2)
    self.assertEqual(min_element_index([1]), 0)
    self.assertEqual(min_element_index([2, 2, 2, 2]), 0)

if __name__ == '__main__':
  unittest.main()