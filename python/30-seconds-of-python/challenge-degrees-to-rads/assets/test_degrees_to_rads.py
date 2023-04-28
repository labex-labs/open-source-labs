import unittest
import sys

sys.path.append("/home/labex/project")
from degrees_to_rads import *
from math import pi


class TestDegreesToRads(unittest.TestCase):
    def test_degrees_to_rads(self):
        self.assertAlmostEqual(degrees_to_rads(0), 0)
        self.assertAlmostEqual(degrees_to_rads(45), pi / 4)
        self.assertAlmostEqual(degrees_to_rads(90), pi / 2)
        self.assertAlmostEqual(degrees_to_rads(180), pi)
        self.assertAlmostEqual(degrees_to_rads(360), 2 * pi)


if __name__ == "__main__":
    unittest.main()
