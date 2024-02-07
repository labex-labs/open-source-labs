# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Implement breadth-first traversal on a binary tree.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume we already have a Node class with an insert method?
  - Yes
- Can we assume this fits in memory?
  - Yes
- What should we do with each node when we process it?
  - Call an input method `visit_func` on the node

## Test Cases

### Breadth-First Traversal

- 5, 2, 8, 1, 3 -> 5, 2, 8, 1, 3

## Algorithm

- Initialize queue with root
- While queue is not empty
  - Dequeue and print the node
  - Queue the left child
  - Queue the right child

Complexity:

- Time: O(n)
- Space: O(n), extra space for the queue

## Code

```python
%run ../bst/bst.py
```

```python
from collections import deque


class BstBfs(Bst):

    def bfs(self, visit_func):
        if self.root is None:
            raise TypeError('root is None')
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            visit_func(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
```

## Unit Test

```python
%run ../utils/results.py
```

```python
%%writefile test_bfs.py
import unittest


class TestBfs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBfs, self).__init__()
        self.results = Results()

    def test_bfs(self):
        bst = BstBfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        bst.bfs(self.results.add_result)
        self.assertEqual(str(self.results), '[5, 2, 8, 1, 3]')

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()
```

    Overwriting test_bfs.py

```python
%run -i test_bfs.py
```

    Success: test_bfs
