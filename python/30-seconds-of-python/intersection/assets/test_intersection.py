import unittest
from intersection import *

class TestIntersection(unittest.TestCase):
    def test_intersection(self):
        self.assertEqual(intersection([1,2,3,4], [3,4,5,6]), [3,4])
        self.assertEqual(intersection([1,2,3], [4,5,6]), [])
        self.assertEqual(intersection([1,2,3], [1,2,3]), [1,2,3])
        self.assertEqual(intersection([], []), [])