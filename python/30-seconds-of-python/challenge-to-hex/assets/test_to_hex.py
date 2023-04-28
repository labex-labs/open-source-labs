import unittest
import sys

sys.path.append("/home/labex/project")
from to_hex import *


class TestToHex(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(to_hex(10), "0xa")

    def test_negative_number(self):
        self.assertEqual(to_hex(-10), "-0xa")

    def test_zero(self):
        self.assertEqual(to_hex(0), "0x0")

    def test_large_number(self):
        self.assertEqual(to_hex(1000000), "0xf4240")


if __name__ == "__main__":
    unittest.main()
