import unittest
import sys

sys.path.append("/home/labex/project")
from head import *


class TestHead(unittest.TestCase):
    def test_head(self):
        self.assertEqual(head([1, 2, 3]), 1)
        self.assertEqual(head([4, 5, 6]), 4)
        self.assertEqual(head(["a", "b", "c"]), "a")
        self.assertEqual(head([True, False, True]), True)


if __name__ == "__main__":
    unittest.main()
