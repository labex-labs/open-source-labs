import unittest
import sys
sys.path.append("/home/labex/project")
from max_element_index import *


class TestMaxElementIndex(unittest.TestCase):
  
  def test_max_element_index(self):
    self.assertEqual(max_element_index([1, 2, 3, 4, 5]), 4)
    self.assertEqual(max_element_index([5, 4, 3, 2, 1]), 0)
    self.assertEqual(max_element_index([1, 3, 2, 5, 4]), 3)
    self.assertEqual(max_element_index([1]), 0)
    self.assertEqual(max_element_index([-1, -2, -3, -4, -5]), 0)
    self.assertEqual(max_element_index([0, 0, 0, 0, 0]), 0)

if __name__ == '__main__':
  unittest.main()