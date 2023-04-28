import unittest
from weighted_average import *


class TestWeightedAverage(unittest.TestCase):
    
    def test_weighted_average(self):
        self.assertAlmostEqual(weighted_average([1, 2, 3], [0.25, 0.25, 0.5]), 2.5)
        self.assertAlmostEqual(weighted_average([4, 5, 6], [0.1, 0.2, 0.7]), 5.5)
        self.assertAlmostEqual(weighted_average([10, 20, 30], [0.5, 0.3, 0.2]), 15.5)
        self.assertAlmostEqual(weighted_average([0, 0, 0], [0.25, 0.25, 0.5]), 0)
        self.assertAlmostEqual(weighted_average([-1, 0, 1], [0.5, 0.25, 0.25]), 0)