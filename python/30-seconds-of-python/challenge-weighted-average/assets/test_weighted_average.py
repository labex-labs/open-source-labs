import unittest
import sys

sys.path.append("/home/labex/project")
from weighted_average import *


class TestWeightedAverage(unittest.TestCase):
    
    def test_weighted_average(self):
        nums = [1, 2, 3]
        weights = [0.6, 0.2, 0.3]
        expected_output = 1.72727
        self.assertAlmostEqual(weighted_average(nums, weights), expected_output, places=5)

if __name__ == "__main__":
    unittest.main()