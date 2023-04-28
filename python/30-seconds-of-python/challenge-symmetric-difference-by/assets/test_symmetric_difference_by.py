import unittest
import sys

sys.path.append("/home/labex/project")
from symmetric_difference_by import *
from math import floor


class TestSymmetricDifferenceBy(unittest.TestCase):
    def test_symmetric_difference_by(self):
        a = [2.1, 1.2]
        b = [2.3, 3.4]
        expected_output = [1.2, 3.4]
        self.assertEqual(symmetric_difference_by(a, b, floor), expected_output)
