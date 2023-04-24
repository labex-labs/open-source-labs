This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Determine the height of a tree.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is this a binary tree?
  - Yes
- Can we assume we already have a Node class with an insert method?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- 5 -> 1
- 5, 2, 8, 1, 3 -> 3

## Algorithm

We'll use a recursive algorithm.

- If the current node is None, return 0
- Else, return 1 + the maximum height of the left or right children

Complexity:

- Time: O(n)
- Space: O(h), where h is the height of the tree

## Code

```python
%run ../bst/bst.py
```

```python
class BstHeight(Bst):

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left),
                       self.height(node.right))
```

## Unit Test

```python
%%writefile test_height.py
import unittest


class TestHeight(unittest.TestCase):

    def test_height(self):
        bst = BstHeight(Node(5))
        self.assertEqual(bst.height(bst.root), 1)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        self.assertEqual(bst.height(bst.root), 3)

        print('Success: test_height')


def main():
    test = TestHeight()
    test.test_height()


if __name__ == '__main__':
    main()
```

    Overwriting test_height.py

```python
%run -i test_height.py
```

    Success: test_height
