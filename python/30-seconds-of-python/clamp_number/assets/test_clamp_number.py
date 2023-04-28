import unittest
import sys
sys.path.append("/home/labex/project")
from clamp_number import *

class TestClampNumber(unittest.TestCase):
  
  def test_clamp_number(self):
    self.assertEqual(clamp_number(5, 1, 10), 5)
    self.assertEqual(clamp_number(15, 1, 10), 10)
    self.assertEqual(clamp_number(-5, 1, 10), 1)
    self.assertEqual(clamp_number(10, 1, 10), 10)
    self.assertEqual(clamp_number(1, 1, 10), 1)
    self.assertEqual(clamp_number(0, -5, 5), 0)
    self.assertEqual(clamp_number(-10, -5, 5), -5)
    self.assertEqual(clamp_number(10, -5, 5), 5)
    
if __name__ == '__main__':
  unittest.main()