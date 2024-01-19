# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Find the lowest common ancestor of two nodes in a binary tree.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is this a binary search tree?
  - No
- Can we assume the two nodes are in the tree?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

```txt
          _10_
        /      \
       5        9
      / \      / \
     12  3    18  20
        / \       /
       1   8     40
```

- 0, 5 -> None
- 5, 0 -> None
- 1, 8 -> 3
- 12, 8 -> 5
- 12, 40 -> 10
- 9, 20 -> 9
- 3, 5 -> 5

## Algorithm

- Verify both nodes are in the tree
- Base cases
  - If the root is None, return None
  - If the root is either node, return the root
- Recursively search left and right
- If the left and right are both nodes
  - The return the root
- Else, left or right, whichever is valid

Complexity:

- Time: O(h), where h is the height of the tree
- Space: O(h), where h is the recursion depth

## Code

```python
class Node(object):

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key)
```

```python
class BinaryTree(object):

    def lca(self, root, node1, node2):
        if None in (root, node1, node2):
            return None
        if (not self._node_in_tree(root, node1) or
                not self._node_in_tree(root, node2)):
            return None
        return self._lca(root, node1, node2)

    def _node_in_tree(self, root, node):
        if root is None:
            return False
        if root is node:
            return True
        left = self._node_in_tree(root.left, node)
        right = self._node_in_tree(root.right, node)
        return left or right

    def _lca(self, root, node1, node2):
        if root is None:
            return None
        if root is node1 or root is node2:
            return root
        left_node = self._lca(root.left, node1, node2)
        right_node = self._lca(root.right, node1, node2)
        if left_node is not None and right_node is not None:
            return root
        else:
            return left_node if left_node is not None else right_node
```

```python
class LcaResult(object):

    def __init__(self, node, is_ancestor):
        self.node = node
        self.is_ancestor = is_ancestor


class BinaryTreeOptimized(object):

    def lca(self, root, node1, node2):
        if root is None:
            raise TypeError('root cannot be None')
        result = self._lca(root, node1, node2)
        if result.is_ancestor:
            return result.node
        return None

    def _lca(self, curr_node, node1, node2):
        if curr_node is None:
            return LcaResult(None, is_ancestor=False)
        if curr_node is node1 and curr_node is node2:
            return LcaResult(curr_node, is_ancestor=True)
        left_result = self._lca(curr_node.left, node1, node2)
        if left_result.is_ancestor:
            return left_result
        right_result = self._lca(curr_node.right, node1, node2)
        if right_result.is_ancestor:
            return right_result
        if left_result.node is not None and right_result.node is not None:
            return LcaResult(curr_node, is_ancestor=True)
        elif curr_node is node1 or curr_node is node2:
            is_ancestor = left_result.node is not None or \
                right_result.node is not None
            return LcaResult(curr_node, is_ancestor)
        else:
            return LcaResult(left_result.node if left_result.node is not None \
                                 else right_result.node, is_ancestor=False)
```

## Unit Test

```python
%%writefile test_lca.py
import unittest


class TestLowestCommonAncestor(unittest.TestCase):

    def test_lca(self):
        node10 = Node(10)
        node5 = Node(5)
        node12 = Node(12)
        node3 = Node(3)
        node1 = Node(1)
        node8 = Node(8)
        node9 = Node(9)
        node18 = Node(18)
        node20 = Node(20)
        node40 = Node(40)
        node3.left = node1
        node3.right = node8
        node5.left = node12
        node5.right = node3
        node20.left = node40
        node9.left = node18
        node9.right = node20
        node10.left = node5
        node10.right = node9
        root = node10
        node0 = Node(0)
        binary_tree = BinaryTree()
        self.assertEqual(binary_tree.lca(root, node0, node5), None)
        self.assertEqual(binary_tree.lca(root, node5, node0), None)
        self.assertEqual(binary_tree.lca(root, node1, node8), node3)
        self.assertEqual(binary_tree.lca(root, node12, node8), node5)
        self.assertEqual(binary_tree.lca(root, node12, node40), node10)
        self.assertEqual(binary_tree.lca(root, node9, node20), node9)
        self.assertEqual(binary_tree.lca(root, node3, node5), node5)
        print('Success: test_lca')


def main():
    test = TestLowestCommonAncestor()
    test.test_lca()


if __name__ == '__main__':
    main()
```

    Overwriting test_lca.py

```python
%run -i test_lca.py
```

    Success: test_lca
