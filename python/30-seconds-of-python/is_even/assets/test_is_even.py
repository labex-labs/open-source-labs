import unittest
from is_even import *

class TestIsEven(unittest.TestCase):
  
  def test_even_number(self):
    self.assertTrue(is_even(4))
  
  def test_odd_number(self):
    self.assertFalse(is_even(3))
  
  def test_zero(self):
    self.assertTrue(is_even(0))
  
  def test_negative_even_number(self):
    self.assertTrue(is_even(-6))
  
  def test_negative_odd_number(self):
    self.assertFalse(is_even(-3))

if __name__ == '__main__':
  unittest.main()