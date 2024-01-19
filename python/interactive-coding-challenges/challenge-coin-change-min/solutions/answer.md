# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Determine the minimum number of ways to make n cents, given coins of denominations less than n cents.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Do the coins have to reach exactly n cents?
  - Yes
- Can we assume we have an infinite number of coins to make n cents?
  - Yes
- Do we need to report the combination(s) of coins that represent the minimum?
  - No
- Can we assume the coin denominations are given in sorted order?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

- coins: None or n: None -> Exception
- coins: [] or n: 0 -> 0
- coins: [1, 2, 3] or [3, 2, 1], n: 5 -> 2

## Algorithm

We'll use top down dynamic programming with memoization.

- Base case: If the total is 0, return 0
- If the total is already in the memo, return it
- For each coin denomination:
  - If this coin > total, continue
  - Recurse, decreasing total by the coin denomination, keeping track of the min return
- Set memo[total] to the min value + 1
- Return the memo[total]

```txt
total: 5
coins: [1,2,3]
memo key: total value: min ways
memo = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2
}
                              5
                           1, 2, 3
                          /
                         4
                      1, 2, 3
                     /
                    3
              1,    2,    3
             /       \     \____
            2         1         0
         1, 2, 3   1, 2, 3
        /   |
       1    0
    1, 2, 3
   /
  0
```

Complexity:

- Time: O(t \* n), where t is the total and n is the number of coin denominations
- Space: O(t) for the recursion depth

## Code

```python
import sys


class CoinChanger(object):

    def make_change(self, coins, total):
        if coins is None or total is None:
            raise TypeError('coins or total cannot be None')
        if not coins or total == 0:
            return 0
        cache = {}
        return self._make_change(coins, total, cache)

    def _make_change(self, coins, total, cache):
        if total == 0:
            return 0
        if total in cache:
            return cache[total]
        min_ways = sys.maxsize
        for coin in coins:
            if total - coin < 0:
                continue
            ways = self._make_change(coins, total - coin, cache)
            if ways < min_ways:
                min_ways = ways
        cache[total] = min_ways + 1
        return cache[total]
```

## Unit Test

```python
%%writefile test_coin_change_min.py
import unittest


class TestCoinChange(unittest.TestCase):

    def test_coin_change(self):
        coin_changer = CoinChanger()
        self.assertRaises(TypeError, coin_changer.make_change, None, None)
        self.assertEqual(coin_changer.make_change([], 0), 0)
        self.assertEqual(coin_changer.make_change([1, 2, 3], 5), 2)
        self.assertEqual(coin_changer.make_change([3, 2, 1], 5), 2)
        self.assertEqual(coin_changer.make_change([3, 2, 1], 8), 3)
        print('Success: test_coin_change')


def main():
    test = TestCoinChange()
    test.test_coin_change()


if __name__ == '__main__':
    main()
```

    Overwriting test_coin_change_min.py

```python
%run -i test_coin_change_min.py
```

    Success: test_coin_change
