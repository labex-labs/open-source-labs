# Solutions

This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Utopian Tree

See the [HackerRank problem page](https://www.hackerrank.com/challenges/utopian-tree).

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

See the [HackerRank problem page](https://www.hackerrank.com/challenges/utopian-tree).

## Test Cases

See the [HackerRank problem page](https://www.hackerrank.com/challenges/utopian-tree).

## Algorithm

- If cycles is 0, return height of 1
- For 1 to cycles:
  - If cycle is odd, double height
  - Else, increment height
- Return height

Complexity:

- Time: O(n)
- Space: O(1)

## Code

```python
class Solution(object):

    def calc_utopian_tree_height(self, cycles):
        height = 1
        if cycles == 0:
            return height
        for i in range(1, cycles+1):
            if i % 2 == 1:
                height *= 2
            else:
                height += 1
        return height
```

## Unit Test

```python
%%writefile test_utopian_tree.py
import unittest


class TestUtopianTree(unittest.TestCase):

    def test_utopian_tree(self):
        solution = Solution()
        self.assertEqual(solution.calc_utopian_tree_height(0), 1)
        self.assertEqual(solution.calc_utopian_tree_height(1), 2)
        self.assertEqual(solution.calc_utopian_tree_height(4), 7)
        print('Success: test_utopian_tree')


def main():
    test = TestUtopianTree()
    test.test_utopian_tree()


if __name__ == '__main__':
    main()
```

    Overwriting test_utopian_tree.py

```python
run -i test_utopian_tree.py
```

    Success: test_utopian_tree
