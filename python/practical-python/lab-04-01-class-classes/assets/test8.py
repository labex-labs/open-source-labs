import sys


sys.path.append("/home/labex/project")
import unittest
from stock import Stock


class TestStock(unittest.TestCase):
    def test_cost(self):
        s = Stock("GOOG", 100, 490.10)
        self.assertEqual(s.cost(), 49010.0)

    def test_sell(self):
        s = Stock("GOOG", 100, 490.10)
        s.sell(25)
        self.assertEqual(s.shares, 75)
        self.assertEqual(s.cost(), 36757.5)


if __name__ == "__main__":
    unittest.main()
