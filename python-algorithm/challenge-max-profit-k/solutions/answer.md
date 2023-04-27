This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Given a list of stock prices on each consecutive day, determine the max profits with k transactions.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is k the number of sell transactions?
  - Yes
- Can we assume the prices input is an array of ints?
  - Yes
- Can we assume the inputs are valid?
  - No
- If the prices are all decreasing and there is no opportunity to make a profit, do we just return 0?
  - Yes
- Should the output be the max profit and days to buy and sell?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
* Prices: None or k: None -> None
* Prices: [] or k <= 0 -> []
* Prices: [0, -1, -2, -3, -4, -5]
    * (max profit, list of transactions)
    * (0, [])
* Prices: [2, 5, 7, 1, 4, 3, 1, 3] k: 3
    * (max profit, list of transactions)
    * (10, [Type.SELL day: 7 price: 3,
            Type.BUY  day: 6 price: 1,
            Type.SELL day: 4 price: 4,
            Type.BUY  day: 3 price: 1,
            Type.SELL day: 2 price: 7,
            Type.BUY  day: 0 price: 2])
```

## Algorithm

We'll use bottom up dynamic programming to build a table.

```txt

The rows (i) represent the prices.
The columns (j) represent the number of transactions (k).

T[i][j] = max(T[i][j - 1],
              prices[j] - price[m] + T[i - 1][m])

m = 0...j-1

      0   1   2   3   4   5   6   7
--------------------------------------
|   | 2 | 5 | 7 | 1 | 4 | 3 | 1 | 3  |
--------------------------------------
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  |
| 1 | 0 | 3 | 5 | 5 | 5 | 5 | 5 | 5  |
| 2 | 0 | 3 | 5 | 5 | 8 | 8 | 8 | 8  |
| 3 | 0 | 3 | 5 | 5 | 8 | 8 | 8 | 10 |
--------------------------------------

Optimization:

max_diff = max(max_diff,
               T[i - 1][j - 1] - prices[j - 1])

T[i][j] = max(T[i][j - 1],
              prices[j] + max_diff)

```

Complexity:

- Time: O(n \* k)
- Space: O(n \* k)

## Code

```python
from enum import Enum  # Python 2 users: Run pip install enum34


class Type(Enum):
    SELL = 0
    BUY = 1


class Transaction(object):

    def __init__(self, type, day, price):
        self.type = type
        self.day = day
        self.price = price

    def __eq__(self, other):
        return self.type == other.type and \
            self.day == other.day and \
            self.price == other.price

    def __repr__(self):
        return str(self.type) + ' day: ' + \
            str(self.day) + ' price: ' + \
            str(self.price)
```

```python
import sys


class StockTrader(object):

    def find_max_profit(self, prices, k):
        if prices is None or k is None:
            raise TypeError('prices or k cannot be None')
        if not prices or k <= 0:
            return []
        num_rows = k + 1  # 0th transaction for dp table
        num_cols = len(prices)
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 or j == 0:
                    T[i][j] = 0
                    continue
                max_profit = -sys.maxsize
                for m in range(j):
                    profit = prices[j] - prices[m] + T[i - 1][m]
                    if profit > max_profit:
                        max_profit = profit
                T[i][j] = max(T[i][j - 1], max_profit)
        return self._find_max_profit_transactions(T, prices)

    def find_max_profit_optimized(self, prices, k):
        if prices is None or k is None:
            raise TypeError('prices or k cannot be None')
        if not prices or k <= 0:
            return []
        num_rows = k + 1
        num_cols = len(prices)
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            max_diff = prices[0] * -1
            for j in range(num_cols):
                if i == 0 or j == 0:
                    T[i][j] = 0
                    continue
                max_diff = max(
                    max_diff,
                    T[i - 1][j - 1] - prices[j - 1])
                T[i][j] = max(
                    T[i][j - 1],
                    prices[j] + max_diff)
        return self._find_max_profit_transactions(T, prices)

    def _find_max_profit_transactions(self, T, prices):
        results = []
        i = len(T) - 1
        j = len(T[0]) - 1
        max_profit = T[i][j]
        while i != 0 and j != 0:
            if T[i][j] == T[i][j - 1]:
                j -= 1
            else:
                sell_price = prices[j]
                results.append(Transaction(Type.SELL, j, sell_price))
                profit = T[i][j] - T[i - 1][j - 1]
                i -= 1
                j -= 1
                for m in range(j + 1)[::-1]:
                    if sell_price - prices[m] == profit:
                        results.append(Transaction(Type.BUY, m, prices[m]))
                        break
        return (max_profit, results)
```

## Unit Test

```python
%%writefile test_max_profit.py
import unittest


class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        stock_trader = StockTrader()
        self.assertRaises(TypeError, stock_trader.find_max_profit, None, None)
        self.assertEqual(stock_trader.find_max_profit(prices=[], k=0), [])
        prices = [5, 4, 3, 2, 1]
        k = 3
        self.assertEqual(stock_trader.find_max_profit(prices, k), (0, []))
        prices = [2, 5, 7, 1, 4, 3, 1, 3]
        profit, transactions = stock_trader.find_max_profit(prices, k)
        self.assertEqual(profit, 10)
        self.assertTrue(Transaction(Type.SELL,
                                day=7,
                                price=3) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                day=6,
                                price=1) in transactions)
        self.assertTrue(Transaction(Type.SELL,
                                day=4,
                                price=4) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                day=3,
                                price=1) in transactions)
        self.assertTrue(Transaction(Type.SELL,
                                day=2,
                                price=7) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                day=0,
                                price=2) in transactions)
        print('Success: test_max_profit')


def main():
    test = TestMaxProfit()
    test.test_max_profit()


if __name__ == '__main__':
    main()
```

    Overwriting test_max_profit.py

```python
%run -i test_max_profit.py
```

    Success: test_max_profit
