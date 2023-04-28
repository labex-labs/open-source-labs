import unittest
from is_weekend import *

from datetime import datetime

class TestIsWeekend(unittest.TestCase):
  
  def test_weekday(self):
    self.assertFalse(is_weekend(datetime(2021, 10, 4))) # Monday
    self.assertFalse(is_weekend(datetime(2021, 10, 5))) # Tuesday
    self.assertFalse(is_weekend(datetime(2021, 10, 6))) # Wednesday
    self.assertFalse(is_weekend(datetime(2021, 10, 7))) # Thursday
    self.assertFalse(is_weekend(datetime(2021, 10, 8))) # Friday
  
  def test_weekend(self):
    self.assertTrue(is_weekend(datetime(2021, 10, 9))) # Saturday
    self.assertTrue(is_weekend(datetime(2021, 10, 10))) # Sunday

if __name__ == '__main__':
  unittest.main()