import unittest
from is_divisible import *


class TestIsDivisible(unittest.TestCase):
  
  def test_divisible(self):
    self.assertTrue(is_divisible(10, 2))
    self.assertTrue(is_divisible(15, 3))
    self.assertTrue(is_divisible(100, 5))
  
  def test_not_divisible(self):
    self.assertFalse(is_divisible(7, 2))
    self.assertFalse(is_divisible(11, 3))
    self.assertFalse(is_divisible(101, 5))
  
  def test_zero_divisor(self):
    with self.assertRaises(ZeroDivisionError):
      is_divisible(10, 0)
  
  def test_negative_dividend(self):
    self.assertTrue(is_divisible(-10, 2))
    self.assertFalse(is_divisible(-10, 3))
  
  def test_negative_divisor(self):
    self.assertTrue(is_divisible(10, -2))
    self.assertFalse(is_divisible(10, -3))
  
if __name__ == '__main__':
  unittest.main()