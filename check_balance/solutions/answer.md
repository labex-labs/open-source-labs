This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Check if a binary tree is balanced.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is a balanced tree one where the heights of two sub trees of any node doesn't differ by more than 1?
  - Yes
- If this is called on a None input, should we raise an exception?
  - Yes
- Can we assume we already have a Node class with an insert method?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- None -> No
- 1 -> Yes
- 5, 3, 8, 1, 4 -> Yes
- 5, 3, 8, 9, 10 -> No

## Algorithm

The algorithm will be similar to where we get the height of a tree as seen in [here](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_height/height_solution.ipynb).

However, we could check whether the tree is balanced while also checking for the heights.

- Base case: If the root is None, return 0
- Recursively check whether the left sub tree is balanced, and get its height left_height
- Recursively check whether the right sub tree is balanced, and get its height right_height
- Compare left_height and right_height
- Return 1 + max(left_height, right_height)

Complexity:

- Time: O(n)
- Space: O(h), where h is the height of the tree

## Code

```python
%run ../bst/bst.py
```

```python
class BstBalance(Bst):

    def _check_balance(self, node):
        if node is None:
            return 0
        left_height = self._check_balance(node.left)
        if left_height == -1:
            return -1
        right_height = self._check_balance(node.right)
        if right_height == -1:
            return -1
        diff = abs(left_height - right_height)
        if diff > 1:
            return -1
        return 1 + max(left_height, right_height)

    def check_balance(self):
        if self.root is None:
            raise TypeError('root cannot be None')
        height = self._check_balance(self.root)
        return height != -1
```

## Unit Test

```python
%%writefile test_check_balance.py
import unittest


class TestCheckBalance(unittest.TestCase):

    def test_check_balance_empty(self):
        bst = BstBalance(None)
        bst.check_balance()

    def test_check_balance(self):
        bst = BstBalance(Node(5))
        self.assertEqual(bst.check_balance(), True)

        bst.insert(3)
        bst.insert(8)
        bst.insert(1)
        bst.insert(4)
        self.assertEqual(bst.check_balance(), True)

        bst = BstBalance(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(9)
        bst.insert(10)
        self.assertEqual(bst.check_balance(), False)

        bst = BstBalance(Node(3))
        bst.insert(2)
        bst.insert(1)
        bst.insert(5)
        bst.insert(4)
        bst.insert(6)
        bst.insert(7)
        self.assertEqual(bst.check_balance(), True)

        print('Success: test_check_balance')


def main():
    test = TestCheckBalance()
    test.assertRaises(TypeError, test.test_check_balance_empty)
    test.test_check_balance()


if __name__ == '__main__':
    main()
```

    Overwriting test_check_balance.py

```python
%run -i test_check_balance.py
```

    Success: test_check_balance
