import unittest
from from_iso_date import *

from datetime import datetime

class TestFromIsoDate(unittest.TestCase):
  
  def test_from_iso_date(self):
    d = '2021-08-31T12:30:45'
    expected_output = datetime(2021, 8, 31, 12, 30, 45)
    self.assertEqual(from_iso_date(d), expected_output)
    
if __name__ == '__main__':
  unittest.main()