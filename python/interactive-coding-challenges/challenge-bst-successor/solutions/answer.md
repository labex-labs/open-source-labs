# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Find the in-order successor of a given node in a binary search tree.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- If there is no successor, do we return None?
  - Yes
- If the input is None, should we throw an exception?
  - Yes
- Can we assume we already have a Node class that keeps track of parents?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
          _5_
        /     \
       3       8
      / \    /   \
     2   4  6    12
    /        \   / \
   1          7 10  15
               /
              9

In: None  Out: Exception
In: 4     Out: 5
In: 5     Out: 6
In: 8     Out: 9
In: 15    Out: None
```

## Algorithm

- If the node has a right subtree, return the left-most node in the right subtree
- Else, go up until you find a node that is its parent's left node
  - If you get to the root (ie node.parent is None), return None
    - The original input node must be the largest in the tree
  - Else, return the parent

Complexity:

- Time: O(h), where h is the height of the tree
- Space: O(h), where h is the recursion depth (tree height), or O(1) if using an iterative approach

## Code

```python
%run ../bst/bst.py
```

```python
class BstSuccessor(object):

    def get_next(self, node):
        if node is None:
            raise TypeError('node cannot be None')
        if node.right is not None:
            return self._left_most(node.right)
        else:
            return self._next_ancestor(node)

    def _left_most(self, node):
        if node.left is not None:
            return self._left_most(node.left)
        else:
            return node.data

    def _next_ancestor(self, node):
        if node.parent is not None:
            if node.parent.data > node.data:
                return node.parent.data
            else:
                return self._next_ancestor(node.parent)
        # We reached the root, the original input node
        # must be the largest element in the tree.
        return None
```

## Unit Test

```python
%%writefile test_bst_successor.py
import unittest


class TestBstSuccessor(unittest.TestCase):

    def test_bst_successor_empty(self):
        bst_successor = BstSuccessor()
        bst_successor.get_next(None)

    def test_bst_successor(self):
        nodes = {}
        node = Node(5)
        nodes[5] = node
        bst = Bst(nodes[5])
        nodes[3] = bst.insert(3)
        nodes[8] = bst.insert(8)
        nodes[2] = bst.insert(2)
        nodes[4] = bst.insert(4)
        nodes[6] = bst.insert(6)
        nodes[12] = bst.insert(12)
        nodes[1] = bst.insert(1)
        nodes[7] = bst.insert(7)
        nodes[10] = bst.insert(10)
        nodes[15] = bst.insert(15)
        nodes[9] = bst.insert(9)

        bst_successor = BstSuccessor()
        self.assertEqual(bst_successor.get_next(nodes[4]), 5)
        self.assertEqual(bst_successor.get_next(nodes[5]), 6)
        self.assertEqual(bst_successor.get_next(nodes[8]), 9)
        self.assertEqual(bst_successor.get_next(nodes[15]), None)

        print('Success: test_bst_successor')


def main():
    test = TestBstSuccessor()
    test.test_bst_successor()
    test.assertRaises(TypeError, test.test_bst_successor_empty)


if __name__ == '__main__':
    main()
```

    Overwriting test_bst_successor.py

```python
%run -i test_bst_successor.py
```

    Success: test_bst_successor
