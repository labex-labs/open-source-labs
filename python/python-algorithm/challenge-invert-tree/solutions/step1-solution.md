This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Invert a binary tree.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- What does it mean to invert a binary tree?
  - Swap all left and right node pairs
- Can we assume we already have a Node class?
  - Yes
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
Input:
     5
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     5
   /   \
  7     2
 / \   / \
9   6 3   1
```

## Algorithm

- Base case
  - If the root is None, return
- Recursive case
  - Recurse on the left node
  - Recurse on the right node
  - Swap left and right
- Return the node

Complexity:

- Time: O(n)
- Space: O(h), where h is the height, for the recursion depth

## Code

```python
%run ../bst/bst.py
```

```python
class InverseBst(Bst):

    def invert_tree(self):
        if self.root is None:
            raise TypeError('root cannot be None')
        return self._invert_tree(self.root)

    def _invert_tree(self, root):
        if root is None:
            return
        self._invert_tree(root.left)
        self._invert_tree(root.right)
        root.left, root.right = root.right, root.left
        return root
```

## Unit Test

```python
%%writefile test_invert_tree.py
import unittest


class TestInvertTree(unittest.TestCase):

    def test_invert_tree(self):
        root = Node(5)
        bst = InverseBst(root)
        node2 = bst.insert(2)
        node3 = bst.insert(3)
        node1 = bst.insert(1)
        node7 = bst.insert(7)
        node6 = bst.insert(6)
        node9 = bst.insert(9)
        result = bst.invert_tree()
        self.assertEqual(result, root)
        self.assertEqual(result.left, node7)
        self.assertEqual(result.right, node2)
        self.assertEqual(result.left.left, node9)
        self.assertEqual(result.left.right, node6)
        self.assertEqual(result.right.left, node3)
        self.assertEqual(result.right.right, node1)
        print('Success: test_invert_tree')


def main():
    test = TestInvertTree()
    test.test_invert_tree()


if __name__ == '__main__':
    main()
```

    Overwriting test_invert_tree.py

```python
%run -i test_invert_tree.py
```

    Success: test_invert_tree
