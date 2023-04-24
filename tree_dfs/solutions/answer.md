This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Implement depth-first traversals (in-order, pre-order, post-order) on a binary tree.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume we already have a Node class with an insert method?
  - Yes
- What should we do with each node when we process it?
  - Call an input method `visit_func` on the node
- Can we assume this fits in memory?
  - Yes

## Test Cases

### In-Order Traversal

- 5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
- 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5

### Pre-Order Traversal

- 5, 2, 8, 1, 3 -> 5, 2, 1, 3, 8
- 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5

### Post-Order Traversal

- 5, 2, 8, 1, 3 -> 1, 3, 2, 8, 5
- 1, 2, 3, 4, 5 -> 5, 4, 3, 2, 1

## Algorithm

## Test Cases

Note:

- This following are all forms of depth-first traversals

### In-Order Traversal

- Recursively call in-order traversal on the left child
- Visit the current node
- Recursively call in-order traversal on the right child

Complexity:

- Time: O(n)
- Space: O(m), where m is the recursion depth, or O(1) if using an iterative approach

### Pre-Order Traversal

- Visit the current node
- Recursively call pre-order traversal on the left child
- Recursively call pre-order traversal on the right child

Complexity:

- Time: O(n)
- Space: O(m), where m is the recursion depth, or O(1) if using an iterative approach

### Post-Order Traversal

- Recursively call post-order traversal on the left child
- Recursively call post-order traversal on the right child
- Visit the current node

Complexity:

- Time: O(n)
- Space: O(m), where m is the recursion depth, or O(1) if using an iterative approach

## Code

```python
%run ../bst/bst.py
```

```python
class BstDfs(Bst):

    def in_order_traversal(self, node, visit_func):
        if node is not None:
            self.in_order_traversal(node.left, visit_func)
            visit_func(node)
            self.in_order_traversal(node.right, visit_func)

    def pre_order_traversal(self, node, visit_func):
        if node is not None:
            visit_func(node)
            self.pre_order_traversal(node.left, visit_func)
            self.pre_order_traversal(node.right, visit_func)

    def post_order_traversal(self, node, visit_func):
        if node is not None:
            self.post_order_traversal(node.left, visit_func)
            self.post_order_traversal(node.right, visit_func)
            visit_func(node)
```

## Unit Test

```python
%run ../utils/results.py
```

```python
%%writefile test_dfs.py
import unittest


class TestDfs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDfs, self).__init__()
        self.results = Results()

    def test_dfs(self):
        bst = BstDfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)

        bst.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 5, 8]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[5, 2, 1, 3, 8]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 3, 2, 8, 5]")
        self.results.clear_results()

        bst = BstDfs(Node(1))
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)

        bst.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[5, 4, 3, 2, 1]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()
```

    Overwriting test_dfs.py

```python
%run -i test_dfs.py
```

    Success: test_dfs
