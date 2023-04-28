import unittest
import sys
sys.path.append("/home/labex/project")
from lcm import *

class TestLCM(unittest.TestCase):
  
  def test_lcm(self):
    self.assertEqual(lcm([2, 3, 4]), 12)
    self.assertEqual(lcm([5, 10, 15]), 30)
    self.assertEqual(lcm([7, 14, 21]), 42)
    self.assertEqual(lcm([8, 12, 16]), 48)
    self.assertEqual(lcm([9, 18, 27]), 54)

if __name__ == '__main__':
  unittest.main()