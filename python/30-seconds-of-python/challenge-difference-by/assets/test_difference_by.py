import unittest
import sys

sys.path.append("/home/labex/project")
from difference_by import *


class TestDifferenceBy(unittest.TestCase):
    def test_difference_by(self):
        a = [2.1, 1.2, 3.3]
        b = [2.3, 3.4]
        fn = lambda x: int(x)
        result = difference_by(a, b, fn)
        self.assertEqual(result, [1.2])


if __name__ == "__main__":
    unittest.main()
