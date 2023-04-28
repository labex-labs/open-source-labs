import unittest
import sys
sys.path.append("/home/labex/project")
from drop_right import *

class TestDropRight(unittest.TestCase):
  
  def test_drop_right(self):
    self.assertEqual(drop_right([1,2,3,4,5]), [1,2,3,4])
    self.assertEqual(drop_right([1,2,3,4,5], 2), [1,2,3])
    self.assertEqual(drop_right([1,2,3,4,5], 5), [])
    self.assertEqual(drop_right([1,2,3,4,5], 6), [])
    self.assertEqual(drop_right([], 2), [])
    
if __name__ == '__main__':
  unittest.main()