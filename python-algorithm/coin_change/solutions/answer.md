This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Determine the total number of unique ways to make n cents, given coins of denominations less than n cents.

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
- coins: [1, 2, 3], n: 5 -> 5

## Algorithm

We'll use a bottom-up dynamic programming approach.

```txt
The rows (i) represent the coin values.
The columns (j) represent the totals.

  -------------------------
  | 0 | 1 | 2 | 3 | 4 | 5 |
  -------------------------
0 | 1 | 0 | 0 | 0 | 0 | 0 |
1 | 1 | 1 | 1 | 1 | 1 | 1 |
2 | 1 | 1 | 2 | 2 | 3 | 3 |
3 | 1 | 1 | 2 | 3 | 4 | 5 |
  -------------------------

Number of ways to get total n with coin[n] equals:
* Number of ways to get total n with coin[n - 1] plus
* Number of ways to get total n - coin[n]

if j == 0:
    T[i][j] = 1
if row == 0:
    T[i][j] = 0
if coins[i] >= j
    T[i][j] = T[i - 1][j] + T[i][j - coins[i]]
else:
    T[i][j] = T[i - 1][j]

The answer will be in the bottom right corner of the matrix.
```

Complexity:

- Time: O(i \* j)
- Space: O(i \* j)

## Code

```python
class CoinChanger(object):

    def make_change(self, coins, total):
        if coins is None or total is None:
            return None
        if not coins or total == 0:
            return 0
        coins = [0] + coins
        num_rows = len(coins)
        num_cols = total + 1
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0:
                    T[i][j] = 0
                    continue
                if j == 0:
                    T[i][j] = 1
                    continue
                if coins[i] <= j:
                    T[i][j] = T[i - 1][j] + T[i][j - coins[i]]
                else:
                    T[i][j] = T[i - 1][j]
        return T[num_rows - 1][num_cols - 1]
```

## Unit Test

```python
%%writefile test_coin_change.py
import unittest


class Challenge(unittest.TestCase):

    def test_coin_change(self):
        coin_changer = CoinChanger()
        self.assertEqual(coin_changer.make_change([1, 2], 0), 0)
        self.assertEqual(coin_changer.make_change([1, 2, 3], 5), 5)
        self.assertEqual(coin_changer.make_change([1, 5, 25, 50], 10), 3)
        print('Success: test_coin_change')


def main():
    test = Challenge()
    test.test_coin_change()


if __name__ == '__main__':
    main()
```

    Overwriting test_coin_change.py

```python
%run -i test_coin_change.py
```

    Success: test_coin_change
