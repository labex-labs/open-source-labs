import unittest
import sys

sys.path.append("/home/labex/project")
from to_iso_date import *
from datetime import datetime


class TestToIsoDate(unittest.TestCase):
    def test_to_iso_date(self):
        d = datetime(2021, 10, 1)
        self.assertEqual(to_iso_date(d), "2021-10-01T00:00:00")

    def test_to_iso_date_with_time(self):
        d = datetime(2021, 10, 1, 12, 30, 45)
        self.assertEqual(to_iso_date(d), "2021-10-01T12:30:45")

    def test_to_iso_date_with_microseconds(self):
        d = datetime(2021, 10, 1, 12, 30, 45, 123456)
        self.assertEqual(to_iso_date(d), "2021-10-01T12:30:45.123456")


if __name__ == "__main__":
    unittest.main()
