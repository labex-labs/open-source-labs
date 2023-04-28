import unittest
from days_diff import *

from datetime import date

def days_diff(start, end):
    return (end - start).days

class TestDaysDiff(unittest.TestCase):
    def test_days_diff(self):
        start = date(2021, 1, 1)
        end = date(2021, 1, 10)
        self.assertEqual(days_diff(start, end), 9)

        start = date(2021, 1, 1)
        end = date(2021, 2, 1)
        self.assertEqual(days_diff(start, end), 31)

        start = date(2021, 1, 1)
        end = date(2022, 1, 1)
        self.assertEqual(days_diff(start, end), 365)

if __name__ == '__main__':
    unittest.main()