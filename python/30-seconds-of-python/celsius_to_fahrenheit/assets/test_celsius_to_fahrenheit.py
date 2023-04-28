import unittest
from celsius_to_fahrenheit import *

class TestCelsiusToFahrenheit(unittest.TestCase):
  
  def test_zero_degrees_celsius(self):
    self.assertEqual(celsius_to_fahrenheit(0), 32)
    
  def test_negative_degrees_celsius(self):
    self.assertEqual(celsius_to_fahrenheit(-10), 14)
    
  def test_positive_degrees_celsius(self):
    self.assertEqual(celsius_to_fahrenheit(20), 68)
    
  def test_decimal_degrees_celsius(self):
    self.assertEqual(celsius_to_fahrenheit(37.5), 99.5)
    
if __name__ == '__main__':
  unittest.main()