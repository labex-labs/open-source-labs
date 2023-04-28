import unittest
import sys

sys.path.append("/home/labex/project")
from last import *


class TestLast(unittest.TestCase):
    def test_last(self):
        self.assertEqual(last([1, 2, 3]), 3)
        self.assertEqual(last([4, 5, 6]), 6)
        self.assertEqual(last(["a", "b", "c"]), "c")
        self.assertEqual(last([True, False, True]), True)


if __name__ == "__main__":
    unittest.main()
