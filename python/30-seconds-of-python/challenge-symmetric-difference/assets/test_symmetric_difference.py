import unittest
import sys
sys.path.append("/home/labex/project")
from symmetric_difference import *

class TestSymmetricDifference(unittest.TestCase):
  
  def test_symmetric_difference(self):
    self.assertEqual(symmetric_difference([1,2,3], [2,3,4]), [1,4])
    self.assertEqual(symmetric_difference([1,2,3], [4,5,6]), [1,2,3,4,5,6])
    self.assertEqual(symmetric_difference([1,2,3], [3,2,1]), [])
    self.assertEqual(symmetric_difference([], []), [])
    self.assertEqual(symmetric_difference([1,2,3], []), [1,2,3])
    self.assertEqual(symmetric_difference([], [4,5,6]), [4,5,6])
    
if __name__ == '__main__':
  unittest.main()