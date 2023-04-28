import unittest
import sys
sys.path.append("/home/labex/project")
from datetime import datetime
from months_diff import months_diff

class TestMonthsDiff(unittest.TestCase):
    def test_months_diff(self):
        start = datetime(2022, 1, 1)
        end = datetime(2022, 4, 1)
        self.assertEqual(months_diff(start, end), 3)

        start = datetime(2022, 1, 1)
        end = datetime(2023, 1, 1)
        self.assertEqual(months_diff(start, end), 13)

        start = datetime(2022, 1, 1)
        end = datetime(2023, 3, 1)
        self.assertEqual(months_diff(start, end), 15)

    def test_months_diff_leap_year(self):
        start = datetime(2020, 2, 1)
        end = datetime(2020, 3, 1)
        self.assertEqual(months_diff(start, end), 1)

        start = datetime(2020, 1, 1)
        end = datetime(2021, 1, 1)
        self.assertEqual(months_diff(start, end), 13)

        start = datetime(2020, 1, 1)
        end = datetime(2022, 1, 1)
        self.assertEqual(months_diff(start, end), 25)

if __name__ == '__main__':
    unittest.main()