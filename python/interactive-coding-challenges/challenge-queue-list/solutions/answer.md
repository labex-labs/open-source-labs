# Solutions

This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Implement a queue with enqueue and dequeue methods using a linked list.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)
- [Pythonic-Code](#Pythonic-Code)

## Constraints

- If there is one item in the list, do you expect the head and tail pointers to both point to it?
  - Yes
- If there are no items on the list, do you expect the head and tail pointers to be None?
  - Yes
- If you dequeue on an empty queue, does that return None?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

### Enqueue

- Enqueue to an empty queue
- Enqueue to a non-empty queue

### Dequeue

- Dequeue an empty queue -> None
- Dequeue a queue with one element
- Dequeue a queue with more than one element

## Algorithm

### Enqueue

- If the list is empty, set head and tail to node
- Else, set tail to node

Complexity:

- Time: O(1)
- Space: O(1)

### Dequeue

- If the list is empty, return None
- If the list has one node
  - Save the head node's value
  - Set head and tail to None
  - Return the saved value
- Else
  - Save the head node's value
  - Set head to its next node
  - Return the saved value

Complexity:

- Time: O(1)
- Space: O(1)

## Code

```python
%%writefile queue_list.py
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        # Empty list
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        # Empty list
        if self.head is None and self.tail is None:
            return None
        data = self.head.data
        # Remove only element from a one element list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return data
```

    Overwriting queue_list.py

```python
%run queue_list.py
```

## Unit Test

```python
%%writefile test_queue_list.py
import unittest


class TestQueue(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Dequeue an empty queue')
        queue = Queue()
        self.assertEqual(queue.dequeue(), None)

        print('Test: Enqueue to an empty queue')
        queue.enqueue(1)

        print('Test: Dequeue a queue with one element')
        self.assertEqual(queue.dequeue(), 1)

        print('Test: Enqueue to a non-empty queue')
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        print('Test: Dequeue a queue with more than one element')
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)

        print('Success: test_end_to_end')


def main():
    test = TestQueue()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
```

    Overwriting test_queue_list.py

```python
%run -i test_queue_list.py
```

    Test: Dequeue an empty queue
    Test: Enqueue to an empty queue
    Test: Dequeue a queue with one element
    Test: Enqueue to a non-empty queue
    Test: Dequeue a queue with more than one element
    Success: test_end_to_end

## Pythonic-Code

Source: https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-queues

```txt
It is possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:

>>>
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```
