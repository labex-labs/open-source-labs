import unittest
import sys
sys.path.append("/home/labex/project")
from cumsum import *
from itertools import accumulate

def cumsum(lst):
  return list(accumulate(lst))

class TestCumsum(unittest.TestCase):
  
  def test_cumsum(self):
    self.assertEqual(cumsum([1,2,3,4]), [1,3,6,10])
    self.assertEqual(cumsum([0,0,0,0]), [0,0,0,0])
    self.assertEqual(cumsum([-1,2,-3,4]), [-1,1,-2,2])
    self.assertEqual(cumsum([1]), [1])

if __name__ == '__main__':
  unittest.main()