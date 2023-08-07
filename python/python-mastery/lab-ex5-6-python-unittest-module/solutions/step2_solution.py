# Step 2 Solution
import stock
import unittest


class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_create_keyword(self):
        s = stock.Stock(name="GOOG", shares=100, price=490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s.cost, 49010.0)

    def test_sell(self):
        s = stock.Stock("GOOG", 100, 490.1)
        s.sell(25)
        self.assertEqual(s.shares, 75)

    def test_from_row(self):
        s = stock.Stock.from_row(["GOOG", "100", "490.1"])
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_repr(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

    def test_eq(self):
        a = stock.Stock("GOOG", 100, 490.1)
        b = stock.Stock("GOOG", 100, 490.1)
        self.assertTrue(a == b)


if __name__ == "__main__":
    unittest.main()
