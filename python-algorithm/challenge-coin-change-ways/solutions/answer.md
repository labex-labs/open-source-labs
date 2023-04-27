This notebook was prepared by [mrb00l34n](http://github.com/mrb00l34n). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Counting Ways of Making Change.

- [Hints](#Hints)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Hints

- Can you think of a way to build up to a solution?
- If there are 2 ways of making 3, and you are now given a coin of value v, how many ways can you make 3 + v?
- Can you think of a way to divide the problem into smaller subproblems?

## Algorithm

One possible solution using dynamic programming:

- Create an array, s.t arr[i] = # of ways to make change for i
- Initialize arr[0] = 1, arr[i>0] = 0
- For each coin, and for each index from coin to n, increment arr[i] by arr[i - coin]

How does this work?

- As we iterate through each coin, we are adding the ways of making arr[i - coin] to arr[i]
- If we have 2 ways of making 4, and are now iterating on a coin of value 3, there should be 2 ways of making 7.
- We are essentially adding the coin we are iterating on to the # of ways of making arr[i].

Complexity:

- Time: O(mn); let the number of coins be m. We iterate from arr[coin] -> arr[n], or ~ n operations on each coin, hence n\*m.
- Space: O(n)

## Code

```python
def change_ways(n, coins):
    arr = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            arr[i] += arr[i - coin]
    return 0 if n == 0 else arr[n]
```

## Unit Test

```python
%%writefile test_coin_change_ways.py
import unittest


class Challenge(unittest.TestCase):

    def test_coin_change_ways(self,solution):
        self.assertEqual(solution(0, [1, 2]), 0)
        self.assertEqual(solution(100, [1, 2, 3]), 884)
        self.assertEqual(solution(1000, range(1, 101)),
                     15658181104580771094597751280645)
        print('Success: test_coin_change_ways')


def main():
    test = Challenge()
    test.test_coin_change_ways(change_ways)


if __name__ == '__main__':
    main()
```

    Overwriting test_coin_change_ways.py

```python
%run -i test_coin_change_ways.py
```

    Success: test_coin_change_ways
