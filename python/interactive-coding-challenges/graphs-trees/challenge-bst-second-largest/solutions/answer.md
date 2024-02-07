# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Find the second largest node in a binary search tree.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- If this is called on a None input or a single node, should we raise an exception?
  - Yes
    - None -> TypeError
    - Single node -> ValueError
- Can we assume we already have a Node class with an insert method?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- None or single node -> Exception

```txt
Input:
                _10_
              _/    \_
             5        15
            / \       / \
           3   8     12  20
          /     \         \
         2       4        30

Output: 20

Input:
                 10
                 /
                5
               / \
              3   7
Output: 7
```

## Algorithm

```txt

If there is no right node, the second largest is the right most left subtree:

                 10
                 /
                5
               / \
              3   7

If there is a right node and the right node has children, recurse to that right child:

                _10_
              _/    \_
             5        15
            / \       / \
           3   8     12  20
          /     \         \
         2       4        30

Eventually we'll get to the following scenario:

                 20
                  \
                   30

If the right node has no children, the second largest is the current node.

```

Complexity:

- Time: O(h)
- Space: O(h), where h is the height of the tree

## Code

```python
%run ../bst/bst.py
```

```python
class Solution(Bst):

    def _find_second_largest(self, node):
        if node.right is not None:
            if node.right.left is not None or node.right.right is not None:
                return self._find_second_largest(node.right)
            else:
                return node
        else:
            return self._find_right_most_node(node.left)

    def _find_right_most_node(self, node):
        if node.right is not None:
            return self._find_right_most_node(node.right)
        else:
            return node

    def find_second_largest(self):
        if self.root is None:
            raise TypeError('root cannot be None')
        if self.root.right is None and self.root.left is None:
            raise ValueError('root must have at least one child')
        return self._find_second_largest(self.root)
```

## Unit Test

```python
%%writefile test_bst_second_largest.py
import unittest


class TestBstSecondLargest(unittest.TestCase):

    def test_bst_second_largest(self):
        bst = Solution(None)
        self.assertRaises(TypeError, bst.find_second_largest)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node15 = bst.insert(15)
        node3 = bst.insert(3)
        node8 = bst.insert(8)
        node12 = bst.insert(12)
        node20 = bst.insert(20)
        node2 = bst.insert(2)
        node4 = bst.insert(4)
        node30 = bst.insert(30)
        self.assertEqual(bst.find_second_largest(), node20)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node3 = bst.insert(3)
        node7 = bst.insert(7)
        self.assertEqual(bst.find_second_largest(), node7)
        print('Success: test_bst_second_largest')


def main():
    test = TestBstSecondLargest()
    test.test_bst_second_largest()


if __name__ == '__main__':
    main()
```

    Overwriting test_bst_second_largest.py

```python
%run -i test_bst_second_largest.py
```

    Success: test_bst_second_largest
