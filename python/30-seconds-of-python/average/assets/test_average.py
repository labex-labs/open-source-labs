import unittest
from average import *

class TestAverage(unittest.TestCase):
  
  def test_average(self):
    self.assertEqual(average(1, 2, 3), 2.0)
    self.assertEqual(average(4, 5, 6, 7), 5.5)
    self.assertEqual(average(0), 0.0)
    self.assertEqual(average(-1, 1), 0.0)
    self.assertEqual(average(2.5, 3.5, 4.5), 3.5)

if __name__ == '__main__':
  unittest.main()