import unittest
import sys
sys.path.append("/home/labex/project")
from to_roman_numeral import *

class TestToRomanNumeral(unittest.TestCase):
  
  def test_to_roman_numeral(self):
    self.assertEqual(to_roman_numeral(1), 'I')
    self.assertEqual(to_roman_numeral(4), 'IV')
    self.assertEqual(to_roman_numeral(9), 'IX')
    self.assertEqual(to_roman_numeral(10), 'X')
    self.assertEqual(to_roman_numeral(40), 'XL')
    self.assertEqual(to_roman_numeral(50), 'L')
    self.assertEqual(to_roman_numeral(90), 'XC')
    self.assertEqual(to_roman_numeral(100), 'C')
    self.assertEqual(to_roman_numeral(400), 'CD')
    self.assertEqual(to_roman_numeral(500), 'D')
    self.assertEqual(to_roman_numeral(900), 'CM')
    self.assertEqual(to_roman_numeral(1000), 'M')
    self.assertEqual(to_roman_numeral(3999), 'MMMCMXCIX')

if __name__ == '__main__':
  unittest.main()