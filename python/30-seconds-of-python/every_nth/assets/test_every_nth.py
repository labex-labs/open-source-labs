import unittest
import sys
sys.path.append("/home/labex/project")
from every_nth import *

def every_nth(lst, nth):
  return lst[nth - 1::nth]

class TestEveryNth(unittest.TestCase):
  
  def test_every_nth(self):
    self.assertEqual(every_nth([1,2,3,4,5,6,7,8,9], 2), [2,4,6,8])
    self.assertEqual(every_nth([1,2,3,4,5,6,7,8,9], 3), [3,6,9])
    self.assertEqual(every_nth([1,2,3,4,5,6,7,8,9], 4), [4,8])
    self.assertEqual(every_nth([1,2,3,4,5,6,7,8,9], 5), [5])
    self.assertEqual(every_nth([1,2,3,4,5,6,7,8,9], 1), [1,2,3,4,5,6,7,8,9])
    
if __name__ == '__main__':
  unittest.main()