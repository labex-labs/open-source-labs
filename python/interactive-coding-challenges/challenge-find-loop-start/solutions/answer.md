# Solution Notebook

This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Find the start of a linked list loop.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is this a singly linked list?
  - Yes
- Can we assume we are always passed a circular linked list?
  - No
- When we find a loop, do we return the node or the node's data?
  - The node
- Can we assume we already have a linked list class that can be used for this problem?
  - Yes

## Test Cases

- Empty list -> None
- Not a circular linked list -> None
  - One element
  - Two or more elements
- Circular linked list general case

## Algorithm

- Use two references `slow`, `fast`, initialized to the `head`
- Increment `slow` and `fast` until they meet
  - `fast` is incremented twice as fast as `slow`
    - If `fast.next` is `None`, we do not have a circular list
- When `slow` and `fast` meet, move `slow` to the `head`
- Increment `slow` and `fast` one node at a time until they meet
- Where they meet is the start of the loop

Complexity:

- Time: O(n)
- Space: O(1)

## Code

```python
%run ../linked_list/linked_list.py
```

```python
class MyLinkedList(LinkedList):

    def find_loop_start(self):
        if self.head is None or self.head.next is None:
            return None
        slow = self.head
        fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                return None
            if slow == fast:
                break
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
        return slow
```

## Unit Test

```python
%%writefile test_find_loop_start.py
import unittest


class TestFindLoopStart(unittest.TestCase):

    def test_find_loop_start(self):
        print('Test: Empty list')
        linked_list = MyLinkedList()
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: One element')
        head = Node(1)
        linked_list = MyLinkedList(head)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Two elements')
        linked_list.append(2)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Three or more elements')
        linked_list.append(3)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: General case: Circular linked list')
        node10 = Node(10)
        node9 = Node(9, node10)
        node8 = Node(8, node9)
        node7 = Node(7, node8)
        node6 = Node(6, node7)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        node0 = Node(0, node1)
        node10.next = node3
        linked_list = MyLinkedList(node0)
        self.assertEqual(linked_list.find_loop_start(), node3)

        print('Success: test_find_loop_start')


def main():
    test = TestFindLoopStart()
    test.test_find_loop_start()


if __name__ == '__main__':
    main()
```

    Overwriting test_find_loop_start.py

```python
%run -i test_find_loop_start.py
```

    Test: Empty list
    Test: Not a circular linked list: One element
    Test: Not a circular linked list: Two elements
    Test: Not a circular linked list: Three or more elements
    Test: General case: Circular linked list
    Success: test_find_loop_start
