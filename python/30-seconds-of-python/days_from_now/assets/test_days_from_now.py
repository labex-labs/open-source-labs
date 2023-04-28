import unittest
from days_from_now import *
from datetime import date, timedelta

def days_from_now(n):
    return date.today() + timedelta(n)

class TestDaysFromNow(unittest.TestCase):
    
    def test_days_from_now_positive(self):
        self.assertEqual(days_from_now(1), date.today() + timedelta(days=1))
        self.assertEqual(days_from_now(7), date.today() + timedelta(days=7))
        self.assertEqual(days_from_now(30), date.today() + timedelta(days=30))
    
    def test_days_from_now_negative(self):
        self.assertEqual(days_from_now(-1), date.today() + timedelta(days=-1))
        self.assertEqual(days_from_now(-7), date.today() + timedelta(days=-7))
        self.assertEqual(days_from_now(-30), date.today() + timedelta(days=-30))
    
    def test_days_from_now_zero(self):
        self.assertEqual(days_from_now(0), date.today())

if __name__ == '__main__':
    unittest.main()