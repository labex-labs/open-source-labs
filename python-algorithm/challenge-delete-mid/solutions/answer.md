This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Delete a node in the middle, given only access to that node.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume this is a non-circular, singly linked list?
  - Yes
- What if the final node is being deleted, do we make it a dummy with value None?
  - Yes
- Can we assume we already have a linked list class that can be used for this problem?
  - Yes

## Test Cases

- Delete on empty list -> None
- Delete None -> None
- Delete on one node -> [None]
- Delete on multiple nodes

## Algorithm

We'll need two pointers, one to the current node and one to the next node. We will copy the next node's data to the current node's data (effectively deleting the current node) and update the current node's next pointer.

- set curr.data to next.data
- set curr.next to next.next

Complexity:

- Time: O(1)
- Space: O(1)

## Code

```python
%run ../linked_list/linked_list.py
```

```python
class MyLinkedList(LinkedList):

    def delete_node(self, node):
        if node is None:
            return
        if node.next is None:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next
```

## Unit Test

```python
%%writefile test_delete_mid.py
import unittest


class TestDeleteNode(unittest.TestCase):

    def test_delete_node(self):
        print('Test: Empty list, null node to delete')
        linked_list = MyLinkedList(None)
        linked_list.delete_node(None)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One node')
        head = Node(2)
        linked_list = MyLinkedList(head)
        linked_list.delete_node(head)
        self.assertEqual(linked_list.get_all_data(), [None])

        print('Test: Multiple nodes')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node1)
        self.assertEqual(linked_list.get_all_data(), [1, 4, 2])

        print('Test: Multiple nodes, delete last element')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node0)
        self.assertEqual(linked_list.get_all_data(), [1, 4, 3, None])

        print('Success: test_delete_node')


def main():
    test = TestDeleteNode()
    test.test_delete_node()


if __name__ == '__main__':
    main()
```

    Overwriting test_delete_mid.py

```python
%run -i test_delete_mid.py
```

    Test: Empty list, null node to delete
    Test: One node
    Test: Multiple nodes
    Test: Multiple nodes, delete last element
    Success: test_delete_node
