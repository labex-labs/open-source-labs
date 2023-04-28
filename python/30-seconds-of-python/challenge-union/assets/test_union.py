import unittest
import sys
sys.path.append("/home/labex/project")
from union import *

class TestUnion(unittest.TestCase):
    def test_union(self):
        self.assertEqual(union([1,2,3], [2,3,4]), [1,2,3,4])
        self.assertEqual(union([1,2,3], [4,5,6]), [1,2,3,4,5,6])
        self.assertEqual(union([], []), [])