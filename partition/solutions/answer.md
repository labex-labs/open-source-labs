This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume this is a non-circular, singly linked list?
  - Yes
- Do we expect the function to return a new list?
  - Yes
- Can we assume the input x is valid?
  - Yes
- Can we assume we already have a linked list class that can be used for this problem?
  - Yes
- Can we create additional data structures?
  - Yes
- Can we assume this fits in memory?
  - Yes

## Test Cases

- Empty list -> []
- One element list -> [element]
- Left linked list is empty
- Right linked list is empty
- General case
  - Partition = 10
  - Input: 4, 3, 13, 8, 10, 1, 10, 12
  - Output: 4, 3, 8, 1, 10, 10, 13, 12

## Algorithm

- Create left and right linked lists
- For each element in the list
  - If elem < x, append to the left list
  - else, append to the right list
- Merge left and right lists

Complexity:

- Time: O(n)
- Space: O(n)

## Code

```python
%run ../linked_list/linked_list.py
```

```python
class MyLinkedList(LinkedList):

    def partition(self, data):
        if self.head is None:
            return
        left = MyLinkedList(None)
        right = MyLinkedList(None)
        curr = self.head

        # Build the left and right lists
        while curr is not None:
            if curr.data < data:
                left.append(curr.data)
            elif curr.data == data:
                right.insert_to_front(curr.data)
            else:
                right.append(curr.data)
            curr = curr.next
        curr_left = left.head
        if curr_left is None:
            return right
        else:
            # Merge the two lists
            while curr_left.next is not None:
                curr_left = curr_left.next
            curr_left.next = right.head
            return left
```

## Unit Test

```python
%%writefile test_partition.py
import unittest


class TestPartition(unittest.TestCase):

    def test_partition(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One element list, left list empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(0)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: Right list is empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: General case')
        # Partition = 10
        # Input: 4, 3, 13, 8, 10, 1, 14, 10, 12
        # Output: 4, 3, 8, 1, 10, 10, 13, 14, 12
        linked_list = MyLinkedList(Node(12))
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(14)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(8)
        linked_list.insert_to_front(13)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(4)
        partitioned_list = linked_list.partition(10)
        self.assertEqual(partitioned_list.get_all_data(),
                     [4, 3, 8, 1, 10, 10, 13, 14, 12])

        print('Success: test_partition')


def main():
    test = TestPartition()
    test.test_partition()


if __name__ == '__main__':
    main()
```

    Overwriting test_partition.py

```python
run -i test_partition.py
```

    Test: Empty list
    Test: One element list, left list empty
    Test: Right list is empty
    Test: General case
    Success: test_partition
