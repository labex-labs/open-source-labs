This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Determine if a tree is a valid binary search tree.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can the tree have duplicates?
  - Yes
- If this is called on a None input, should we raise an exception?
  - Yes
- Can we assume we already have a Node class?
  - Yes
- Can we assume this fits in memory?
  - Yes

## Test Cases

None -> exception

```txt
Valid:
      5
    /   \
   5     8
  /     /
 4     6
        \
         7
        
Invalid:
      5
    /   \
   5     8
    \   
    20
```

## Algorithm

We'll use a recursive solution that validates left <= current < right, passing down the min and max values as we do a depth-first traversal.

- If the node is None, return True
- If min is set and the node's value <= min, return False
- if max is set and the node's value > max, return False
- Recursively call the validate function on node.left, updating max
- Recursively call the validate function on node.right, updating min

Complexity:

- Time: O(n)
- Space: O(h), where h is the height of the tree

## Code

```python
%run ../bst/bst.py
```

```python
import sys


class BstValidate(Bst):

    def validate(self):
        if self.root is None:
            raise TypeError('No root node')
        return self._validate(self.root)

    def _validate(self, node, minimum=-sys.maxsize, maximum=sys.maxsize):
        if node is None:
            return True
        if node.data <= minimum or node.data > maximum:
            return False
        if not self._validate(node.left, minimum, node.data):
            return False
        if not self._validate(node.right, node.data, maximum):
            return False
        return True
```

## Unit Test

```python
%%writefile test_bst_validate.py
import unittest


class TestBstValidate(unittest.TestCase):

    def test_bst_validate_empty(self):
        bst = BstValidate(None)
        bst.validate()

    def test_bst_validate(self):
        bst = BstValidate(Node(5))
        bst.insert(8)
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(7)
        self.assertEqual(bst.validate(), True)

        bst = BstValidate(Node(5))
        left = Node(5)
        right = Node(8)
        invalid = Node(20)
        bst.root.left = left
        bst.root.right = right
        bst.root.left.right = invalid
        self.assertEqual(bst.validate(), False)

        print('Success: test_bst_validate')


def main():
    test = TestBstValidate()
    test.assertRaises(TypeError, test.test_bst_validate_empty)
    test.test_bst_validate()


if __name__ == '__main__':
    main()
```

    Overwriting test_bst_validate.py

```python
%run -i test_bst_validate.py
```

    Success: test_bst_validate
