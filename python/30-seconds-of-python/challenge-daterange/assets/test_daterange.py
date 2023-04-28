import unittest
import sys

sys.path.append("/home/labex/project")
from daterange import *
from datetime import date, timedelta


def daterange(start, end):
    return [start + timedelta(n) for n in range(int((end - start).days))]


class TestDateRange(unittest.TestCase):
    def test_date_range(self):
        start_date = date(2021, 1, 1)
        end_date = date(2021, 1, 5)
        expected_output = [
            date(2021, 1, 1),
            date(2021, 1, 2),
            date(2021, 1, 3),
            date(2021, 1, 4),
        ]
        self.assertEqual(daterange(start_date, end_date), expected_output)


if __name__ == "__main__":
    unittest.main()
