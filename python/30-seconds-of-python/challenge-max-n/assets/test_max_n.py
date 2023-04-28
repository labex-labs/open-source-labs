import unittest
import sys
sys.path.append("/home/labex/project")
from max_n import *

class TestMaxN(unittest.TestCase):
  
  def test_max_n(self):
    self.assertEqual(max_n([1, 2, 3, 4, 5]), [5])
    self.assertEqual(max_n([1, 2, 3, 4, 5], 3), [5, 4, 3])
    self.assertEqual(max_n([5, 4, 3, 2, 1], 2), [5, 4])
    self.assertEqual(max_n([1, 1, 1, 1, 1]), [1])
    self.assertEqual(max_n([1]), [1])
    
if __name__ == '__main__':
  unittest.main()