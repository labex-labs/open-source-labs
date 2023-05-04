import unittest
import sys

sys.path.append("/home/labex/project")
from count_occurrences import *


class TestCountOccurrences(unittest.TestCase):
    def test_count_occurrences(self):
        self.assertEqual(count_occurrences([1, 2, 3, 4, 5], 3), 1)
        self.assertEqual(count_occurrences([1, 2, 3, 3, 3, 4, 5], 3), 3)
        self.assertEqual(count_occurrences(["a", "b", "c", "c", "d"], "c"), 2)
        self.assertEqual(count_occurrences([], 5), 0)
        self.assertEqual(count_occurrences([True, False, True], False), 1)


if __name__ == "__main__":
    unittest.main()
