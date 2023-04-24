This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Implement a min heap with extract_min and insert methods.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume the inputs are ints?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- Extract min of an empty tree
- Extract min general case
- Insert into an empty tree
- Insert general case (left and right insert)

```txt
          _5_
        /     \
       20     15
      / \    /  \
     22  40 25
     
extract_min(): 5

          _15_
        /      \
       20      25
      / \     /  \
     22  40 

insert(2):

          _2_
        /     \
       20      5
      / \     / \
     22  40  25  15
```

## Algorithm

A heap is a complete binary tree where each node is smaller than its children.

### extract_min

```txt
          _5_
        /     \
       20     15
      / \    /  \
     22  40 25

Save the root as the value to be returned: 5
Move the right most element to the root: 25

          _25_
        /      \
       20      15
      / \     /  \
     22  40 

Bubble down 25: Swap 25 and 15 (the smaller child)

          _15_
        /      \
       20      25
      / \     /  \
     22  40 

Return 5
```

We'll use an array to represent the tree, here are the indices:

```txt
          _0_
        /     \
       1       2
      / \     / \
     3   4   
```

To get to a child, we take 2 _ index + 1 (left child) or 2 _ index + 2 (right child).

For example, the right child of index 1 is 2 \* 1 + 2 = 4.

Complexity:

- Time: O(lg(n))
- Space: O(lg(n)) for the recursion depth (tree height), or O(1) if using an iterative approach

### insert

```txt
          _5_
        /     \
       20     15
      / \    /  \
     22  40 25

insert(2):
Insert at the right-most spot to maintain the heap property.

          _5_
        /     \
       20     15
      / \    /  \
     22  40 25   2

Bubble up 2: Swap 2 and 15

          _5_
        /     \
       20     2
      / \    / \
     22  40 25  15

Bubble up 2: Swap 2 and 5

          _2_
        /     \
       20     5
      / \    / \
     22  40 25  15
```

We'll use an array to represent the tree, here are the indices:

```txt
          _0_
        /     \
       1       2
      / \     / \
     3   4   5   6
```

To get to a parent, we take (index - 1) // 2.

For example, the parent of index 6 is (6 - 1) // 2 = 2.

Complexity:

- Time: O(lg(n))
- Space: O(lg(n)) for the recursion depth (tree height), or O(1) if using an iterative approach

## Code

```python
%%writefile min_heap.py
from __future__ import division

import sys


class MinHeap(object):

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def extract_min(self):
        if not self.array:
            return None
        if len(self.array) == 1:
            return self.array.pop(0)
        minimum = self.array[0]
        # Move the last element to the root
        self.array[0] = self.array.pop(-1)
        self._bubble_down(index=0)
        return minimum

    def peek_min(self):
        return self.array[0] if self.array else None

    def insert(self, key):
        if key is None:
            raise TypeError('key cannot be None')
        self.array.append(key)
        self._bubble_up(index=len(self.array) - 1)

    def _bubble_up(self, index):
        if index == 0:
            return
        index_parent = (index - 1) // 2
        if self.array[index] < self.array[index_parent]:
            # Swap the indices and recurse
            self.array[index], self.array[index_parent] = \
                self.array[index_parent], self.array[index]
            self._bubble_up(index_parent)

    def _bubble_down(self, index):
        min_child_index = self._find_smaller_child(index)
        if min_child_index == -1:
            return
        if self.array[index] > self.array[min_child_index]:
            # Swap the indices and recurse
            self.array[index], self.array[min_child_index] = \
                self.array[min_child_index], self.array[index]
            self._bubble_down(min_child_index)

    def _find_smaller_child(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        # No right child
        if right_child_index >= len(self.array):
            # No left child
            if left_child_index >= len(self.array):
                return -1
            # Left child only
            else:
                return left_child_index
        else:
            # Compare left and right children
            if self.array[left_child_index] < self.array[right_child_index]:
                return left_child_index
            else:
                return right_child_index
```

    Overwriting min_heap.py

```python
%run min_heap.py
```

## Unit Test

```python
%%writefile test_min_heap.py
import unittest


class TestMinHeap(unittest.TestCase):

    def test_min_heap(self):
        heap = MinHeap()
        self.assertEqual(heap.peek_min(), None)
        self.assertEqual(heap.extract_min(), None)
        heap.insert(20)
        self.assertEqual(heap.array[0], 20)
        heap.insert(5)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        heap.insert(15)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 15)
        heap.insert(22)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 15)
        self.assertEqual(heap.array[3], 22)
        heap.insert(40)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 15)
        self.assertEqual(heap.array[3], 22)
        self.assertEqual(heap.array[4], 40)
        heap.insert(3)
        self.assertEqual(heap.array[0], 3)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 5)
        self.assertEqual(heap.array[3], 22)
        self.assertEqual(heap.array[4], 40)
        self.assertEqual(heap.array[5], 15)
        mins = []
        while heap:
            mins.append(heap.extract_min())
        self.assertEqual(mins, [3, 5, 15, 20, 22, 40])
        print('Success: test_min_heap')


def main():
    test = TestMinHeap()
    test.test_min_heap()


if __name__ == '__main__':
    main()
```

    Overwriting test_min_heap.py

```python
%run -i test_min_heap.py
```

    Success: test_min_heap
