import unittest
import sys

sys.path.append("/home/labex/project")
from compact import *


class TestCompact(unittest.TestCase):
    def test_compact(self):
        self.assertEqual(compact([0, 1, False, 2, "", 3]), [1, 2, 3])
        self.assertEqual(compact([None, 0, "", False, [], {}]), [])
        self.assertEqual(compact([1, 2, 3]), [1, 2, 3])
        self.assertEqual(compact([]), [])


if __name__ == "__main__":
    unittest.main()