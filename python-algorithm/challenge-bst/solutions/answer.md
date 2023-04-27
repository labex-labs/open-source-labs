This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Implement a binary search tree with an insert method.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we insert None values?
  - No
- Can we assume we are working with valid integers?
  - Yes
- Can we assume all left descendents <= n < all right descendents?
  - Yes
- Do we have to keep track of the parent nodes?
  - This is optional
- Can we assume this fits in memory?
  - Yes

## Test Cases

### Insert

Insert will be tested through the following traversal:

### In-Order Traversal

- 5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
- 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5

If the `root` input is `None`, return a tree with the only element being the new root node.

You do not have to code the in-order traversal, it is part of the unit test.

## Algorithm

### Insert

- If the root is None, return Node(data)
- If the data is <= the current node's data
  - If the current node's left child is None, set it to Node(data)
  - Else, recursively call insert on the left child
- Else
  - If the current node's right child is None, set it to Node(data)
  - Else, recursively call insert on the right child

Complexity:

- Time: O(h), where h is the height of the tree
  - In a balanced tree, the height is O(log(n))
  - In the worst case we have a linked list structure with O(n)
- Space: O(m), where m is the recursion depth, or O(1) if using an iterative approach

## Code

```python
%%writefile bst.py
class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)


class Bst(object):

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            if node.left is None:
                node.left = self._insert(node.left, data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = self._insert(node.right, data)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, data)
```

    Overwriting bst.py

```python
%run bst.py
```

## Unit Test

```python
%run dfs.py
```

```python
%run ../utils/results.py
```

```python
%%writefile test_bst.py
import unittest


class TestTree(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTree, self).__init__()
        self.results = Results()

    def test_tree_one(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), '[1, 2, 3, 5, 8]')
        self.results.clear_results()

    def test_tree_two(self):
        bst = Bst()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), '[1, 2, 3, 4, 5]')

        print('Success: test_tree')


def main():
    test = TestTree()
    test.test_tree_one()
    test.test_tree_two()


if __name__ == '__main__':
    main()
```

    Overwriting test_bst.py

```python
%run -i test_bst.py
```

    Success: test_tree
