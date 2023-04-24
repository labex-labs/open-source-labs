This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Implement a linked list with insert, append, find, delete, length, and print methods.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume this is a non-circular, singly linked list?
  - Yes
- Do we keep track of the tail or just the head?
  - Just the head
- Can we insert None values?
  - No

## Test Cases

### Insert to Front

- Insert a None
- Insert in an empty list
- Insert in a list with one element or more elements

### Append

- Append a None
- Append in an empty list
- Insert in a list with one element or more elements

### Find

- Find a None
- Find in an empty list
- Find in a list with one element or more matching elements
- Find in a list with no matches

### Delete

- Delete a None
- Delete in an empty list
- Delete in a list with one element or more matching elements
- Delete in a list with no matches

### Length

- Length of zero or more elements

### Print

- Print an empty list
- Print a list with one or more elements

## Algorithm

### Insert to Front

- If the data we are inserting is None, return
- Create a node with the input data, set node.next to head
- Assign the head to the node

Complexity:

- Time: O(1)
- Space: O(1)

### Append

- If the data we are inserting is None, return
- Create a node with the input data
- If this is an empty list
  - Assign the head to the node
- Else
  - Iterate to the end of the list
  - Set the final node's next to the new node

Complexity:

- Time: O(n)
- Space: O(1)

### Find

- If data we are finding is None, return
- If the list is empty, return
- For each node
  - If the value is a match, return it
  - Else, move on to the next node

Complexity:

- Time: O(n)
- Space: O(1)

### Delete

- If data we are deleting is None, return
- If the list is empty, return
- For each node, keep track of previous and current node
  - If the value we are deleting is a match in the current node
    - Update previous node's next pointer to the current node's next pointer
    - We do not have have to explicitly delete in Python
  - Else, move on to the next node
- As an alternative, we could avoid the use of two pointers by evaluating the current node's next value:
  - If the next value is a match, set the current node's next to next.next
  - Special care should be taken if deleting the head node

Complexity:

- Time: O(n)
- Space: O(1)

### Length

- For each node
  - Increase length counter

Complexity:

- Time: O(n)
- Space: O(1)

### Print

- For each node
  - Print the node's value

Complexity:

- Time: O(n)
- Space: O(1)

## Code

```python
%%writefile linked_list.py
class Node(object):

    def __init__(self, data, next=None):
        self.next = next
        self.data = data

    def __str__(self):
        return self.data


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def insert_to_front(self, data):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def append(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    def find(self, data):
        if data is None:
            return None
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node
            curr_node = curr_node.next
        return None

    def delete(self, data):
        if data is None:
            return
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next

    def delete_alt(self, data):
        if data is None:
            return
        if self.head is None:
            return
        curr_node = self.head
        if curr_node.data == data:
            curr_node = curr_node.next
            return
        while curr_node.next is not None:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def get_all_data(self):
        data = []
        curr_node = self.head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data
```

    Overwriting linked_list.py

```python
%run linked_list.py
```

## Unit Test

```python
%%writefile test_linked_list.py
import unittest


class TestLinkedList(unittest.TestCase):

    def test_insert_to_front(self):
        print('Test: insert_to_front on an empty list')
        linked_list = LinkedList(None)
        linked_list.insert_to_front(10)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: insert_to_front on a None')
        linked_list.insert_to_front(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: insert_to_front general case')
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(linked_list.get_all_data(), ['bc', 'a', 10])

        print('Success: test_insert_to_front\n')

    def test_append(self):
        print('Test: append on an empty list')
        linked_list = LinkedList(None)
        linked_list.append(10)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: append a None')
        linked_list.append(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: append general case')
        linked_list.append('a')
        linked_list.append('bc')
        self.assertEqual(linked_list.get_all_data(), [10, 'a', 'bc'])

        print('Success: test_append\n')

    def test_find(self):
        print('Test: find on an empty list')
        linked_list = LinkedList(None)
        node = linked_list.find('a')
        self.assertEqual(node, None)

        print('Test: find a None')
        head = Node(10)
        linked_list = LinkedList(head)
        node = linked_list.find(None)
        self.assertEqual(node, None)

        print('Test: find general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        node = linked_list.find('a')
        self.assertEqual(str(node), 'a')

        print('Test: find general case with no matches')
        node = linked_list.find('aaa')
        self.assertEqual(node, None)

        print('Success: test_find\n')

    def test_delete(self):
        print('Test: delete on an empty list')
        linked_list = LinkedList(None)
        linked_list.delete('a')
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: delete a None')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.delete(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: delete general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        linked_list.delete('a')
        self.assertEqual(linked_list.get_all_data(), ['bc', 10])

        print('Test: delete general case with no matches')
        linked_list.delete('aa')
        self.assertEqual(linked_list.get_all_data(), ['bc', 10])

        print('Success: test_delete\n')

    def test_len(self):
        print('Test: len on an empty list')
        linked_list = LinkedList(None)
        self.assertEqual(len(linked_list), 0)

        print('Test: len general case')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(len(linked_list), 3)

        print('Success: test_len\n')


def main():
    test = TestLinkedList()
    test.test_insert_to_front()
    test.test_append()
    test.test_find()
    test.test_delete()
    test.test_len()


if __name__ == '__main__':
    main()
```

    Overwriting test_linked_list.py

```python
%run -i test_linked_list.py
```

    Test: insert_to_front on an empty list
    Test: insert_to_front on a None
    Test: insert_to_front general case
    Success: test_insert_to_front

    Test: append on an empty list
    Test: append a None
    Test: append general case
    Success: test_append

    Test: find on an empty list
    Test: find a None
    Test: find general case with matches
    Test: find general case with no matches
    Success: test_find

    Test: delete on an empty list
    Test: delete a None
    Test: delete general case with matches
    Test: delete general case with no matches
    Success: test_delete

    Test: len on an empty list
    Test: len general case
    Success: test_len
