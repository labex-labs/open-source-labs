import unittest
import sys

sys.path.append("/home/labex/project")
from intersection_by import *


class TestIntersectionBy(unittest.TestCase):
    def test_intersection_by(self):
        a = [1, 2, 3, 4, 5]
        b = [2, 4, 6, 8, 10]
        fn = lambda x: x * 2
        self.assertEqual(intersection_by(a, b, fn), [1, 2, 3, 4, 5])
