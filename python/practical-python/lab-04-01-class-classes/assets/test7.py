import sys


sys.path.append("/home/labex/project")
import unittest
from stock import Stock


class TestStock(unittest.TestCase):
    def test_cost(self):
        s = Stock("GOOG", 100, 490.10)
        self.assertEqual(s.shares, 100)


if __name__ == "__main__":
    unittest.main()
