import unittest
import sys

sys.path.append("/home/labex/project")
from similarity import *


class TestSimilarity(unittest.TestCase):
    def test_similarity(self):
        self.assertEqual(similarity([1, 2, 3], [2, 3, 4]), [2, 3])
        self.assertEqual(similarity(["a", "b", "c"], ["b", "c", "d"]), ["b", "c"])
        self.assertEqual(similarity([], []), [])
        self.assertEqual(similarity([1, 2, 3], []), [])
        self.assertEqual(similarity([], [1, 2, 3]), [])


if __name__ == "__main__":
    unittest.main()
