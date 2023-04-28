import unittest
import sys
sys.path.append("/home/labex/project")
from fahrenheit_to_celsius import *

class TestFahrenheitToCelsius(unittest.TestCase):
  
  def test_positive_degrees(self):
    self.assertEqual(fahrenheit_to_celsius(32), 0)
    self.assertEqual(fahrenheit_to_celsius(68), 20)
    self.assertEqual(fahrenheit_to_celsius(212), 100)
  
  def test_negative_degrees(self):
    self.assertEqual(fahrenheit_to_celsius(-40), -40)
    self.assertEqual(fahrenheit_to_celsius(-22), -30)
    self.assertEqual(fahrenheit_to_celsius(-4), -20)
  
  def test_decimal_degrees(self):
    self.assertAlmostEqual(fahrenheit_to_celsius(77), 25, places=2)
    self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37, places=2)
    self.assertAlmostEqual(fahrenheit_to_celsius(104), 40, places=2)

if __name__ == '__main__':
  unittest.main()