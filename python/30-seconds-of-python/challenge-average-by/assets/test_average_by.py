import unittest
import sys

sys.path.append("/home/labex/project")
from average_by import *


class TestAverageBy(unittest.TestCase):
    def test_average_by(self):
        self.assertEqual(average_by([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(average_by([1, 2, 3, 4, 5], lambda x: x**2), 11.0)
        self.assertEqual(average_by([1, 2, 3, 4, 5], lambda x: x * 2), 6.0)
        self.assertEqual(average_by([1, 2, 3, 4, 5], lambda x: x / 2), 1.5)
        self.assertEqual(average_by([1, 2, 3, 4, 5], lambda x: x + 1), 4.0)


if __name__ == "__main__":
    unittest.main()
