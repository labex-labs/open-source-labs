import unittest
import sys
sys.path.append("/home/labex/project")
from arithmetic_progression import *

class TestArithmeticProgression(unittest.TestCase):
  
  def test_arithmetic_progression(self):
    self.assertEqual(arithmetic_progression(2, 10), [2, 4, 6, 8, 10])
    self.assertEqual(arithmetic_progression(3, 15), [3, 6, 9, 12, 15])
    self.assertEqual(arithmetic_progression(5, 25), [5, 10, 15, 20, 25])
    self.assertEqual(arithmetic_progression(7, 28), [7, 14, 21, 28])
    self.assertEqual(arithmetic_progression(1, 10), list(range(1, 11)))
    
if __name__ == '__main__':
  unittest.main()