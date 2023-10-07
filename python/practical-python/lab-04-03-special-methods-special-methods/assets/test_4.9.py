import sys

sys.path.append("/home/labex/project")

import stock
import unittest


class StockTest(unittest.TestCase):
    def test_repr(self):
        goog = stock.Stock("GOOG", 100, 490.1)
        expected_repr = "Stock('GOOG', 100, 490.1)"
        actual_repr = repr(goog)
        self.assertEqual(actual_repr, expected_repr)


if __name__ == "__main__":
    unittest.main()
