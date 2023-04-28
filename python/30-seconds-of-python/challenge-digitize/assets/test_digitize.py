import unittest
import sys

sys.path.append("/home/labex/project")
from digitize import *


def digitize(n):
    return list(map(int, str(n)))


class TestDigitize(unittest.TestCase):
    def test_digitize(self):
        self.assertEqual(digitize(123), [1, 2, 3])
        self.assertEqual(digitize(456), [4, 5, 6])
        self.assertEqual(digitize(789), [7, 8, 9])
        self.assertEqual(digitize(0), [0])
        self.assertEqual(digitize(987654321), [9, 8, 7, 6, 5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
