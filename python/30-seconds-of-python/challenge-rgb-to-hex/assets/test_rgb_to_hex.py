import unittest
import sys

sys.path.append("/home/labex/project")
from rgb_to_hex import *


class TestRGBtoHex(unittest.TestCase):
    def test_rgb_to_hex(self):
        self.assertEqual(rgb_to_hex(255, 255, 255), "FFFFFF")
        self.assertEqual(rgb_to_hex(0, 0, 0), "000000")
        self.assertEqual(rgb_to_hex(255, 0, 0), "FF0000")
        self.assertEqual(rgb_to_hex(0, 255, 0), "00FF00")
        self.assertEqual(rgb_to_hex(0, 0, 255), "0000FF")


if __name__ == "__main__":
    unittest.main()
