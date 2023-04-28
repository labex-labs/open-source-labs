import unittest
import sys

sys.path.append("/home/labex/project")
from rads_to_degrees import *
from math import pi


def rads_to_degrees(rad):
    return (rad * 180.0) / pi


class TestRadsToDegrees(unittest.TestCase):
    def test_rads_to_degrees(self):
        self.assertAlmostEqual(rads_to_degrees(0), 0)
        self.assertAlmostEqual(rads_to_degrees(pi / 2), 90)
        self.assertAlmostEqual(rads_to_degrees(pi), 180)
        self.assertAlmostEqual(rads_to_degrees(3 * pi / 2), 270)
        self.assertAlmostEqual(rads_to_degrees(2 * pi), 360)


if __name__ == "__main__":
    unittest.main()
