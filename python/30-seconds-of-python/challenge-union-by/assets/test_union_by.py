import unittest
import sys

sys.path.append("/home/labex/project")
from union_by import *
from math import floor


class TestUnionBy(unittest.TestCase):
    
    def test_union_by(self):
        a = [2.1]
        b = [1.2, 2.3]
        expected_output = [1.2, 2.1]
        self.assertEqual(union_by(a, b, floor), expected_output)


if __name__ == "__main__":
    unittest.main()