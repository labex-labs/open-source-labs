import unittest
import sys
sys.path.append("/home/labex/project")
from is_weekday import *
from datetime import datetime

class TestIsWeekday(unittest.TestCase):
  
  def test_weekday(self):
    self.assertTrue(is_weekday(datetime(2021, 7, 12))) # Monday
    self.assertTrue(is_weekday(datetime(2021, 7, 13))) # Tuesday
    self.assertTrue(is_weekday(datetime(2021, 7, 14))) # Wednesday
    self.assertTrue(is_weekday(datetime(2021, 7, 15))) # Thursday
    self.assertTrue(is_weekday(datetime(2021, 7, 16))) # Friday
  
  def test_weekend(self):
    self.assertFalse(is_weekday(datetime(2021, 7, 17))) # Saturday
    self.assertFalse(is_weekday(datetime(2021, 7, 18))) # Sunday

if __name__ == '__main__':
  unittest.main()