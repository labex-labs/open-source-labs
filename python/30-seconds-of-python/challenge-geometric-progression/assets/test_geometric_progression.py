import unittest
import sys

sys.path.append("/home/labex/project")
from geometric_progression import *


class TestGeometricProgression(unittest.TestCase):
    def test_geometric_progression(self):
        self.assertEqual(geometric_progression(10), [1, 2, 4, 8])
        self.assertEqual(geometric_progression(20), [1, 2, 4, 8, 16])
        self.assertEqual(geometric_progression(30, 3, 3), [3, 9, 27])


if __name__ == "__main__":
    unittest.main()
