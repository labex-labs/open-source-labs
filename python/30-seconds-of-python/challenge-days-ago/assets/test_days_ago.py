import unittest
import sys
sys.path.append("/home/labex/project")
from days_ago import *
from datetime import date, timedelta

def days_ago(n):
    return date.today() - timedelta(n)

class TestDaysAgo(unittest.TestCase):
    def test_days_ago(self):
        self.assertEqual(days_ago(1), date.today() - timedelta(1))
        self.assertEqual(days_ago(7), date.today() - timedelta(7))
        self.assertEqual(days_ago(30), date.today() - timedelta(30))
        self.assertEqual(days_ago(365), date.today() - timedelta(365))

if __name__ == '__main__':
    unittest.main()