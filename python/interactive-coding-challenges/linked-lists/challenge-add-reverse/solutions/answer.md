# Solutions

This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Add two numbers whose digits are stored in a linked list in reverse order.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume this is a non-circular, singly linked list?
  - Yes
- Do we expect the return to be in reverse order too?
  - Yes
- What if one of the inputs is None?
  - Return None for an invalid operation
- How large are these numbers--can they fit in memory?
  - Yes
- Can we assume we already have a linked list class that can be used for this problem?
  - Yes
- Can we assume this fits in memory?
  - Yes

## Test Cases

- Empty list(s) -> None
- Add values of different lengths
  - Input 1: 6->5->None
  - Input 2: 9->8->7
  - Result: 5->4->8
- Add values of same lengths
  - Exercised from values of different lengths
  - Done here for completeness

## Algorithm

We could solve this with an iterative or a recursive algorithm, both are well suited for this exercise. We'll use a recursive algorithm for practice with recursion. Note this takes an extra space of O(m) where m is the recursion depth.

- Base case:
  - if first and second lists are None AND carry is zero
    - Return None
- Recursive case:
  - Set `value` to `carry`
  - Add both nodes' `data` to `value`
  - Set the `carry` to 1 if `value >= 10, else 0`
  - Set the `remainder` to `value % 10`
  - Create a `node` with the `remainder`
  - Set `node.next` to a recursive call on the `next` nodes, passing in the `carry`
  - Return `node`

Complexity:

- Time: O(n)
- Space: O(m), extra space for result and recursion depth

Notes:

- Careful with adding if the lists differ
  - Only add if a node is not None
  - Alternatively, we could add trailing zeroes to the smaller list

## Code

```python
%run ../linked_list/linked_list.py
```

```python
class MyLinkedList(LinkedList):

    def _add_reverse(self, first_node, second_node, carry):
        # Base case
        if first_node is None and second_node is None and not carry:
            return None

        # Recursive case
        value = carry
        value += first_node.data if first_node is not None else 0
        value += second_node.data if second_node is not None else 0
        carry = 1 if value >= 10 else 0
        value %= 10
        node = Node(value)
        node.next = self._add_reverse(
            first_node.next if first_node is not None else None,
            second_node.next if first_node is not None else None,
            carry)
        return node

    def add_reverse(self, first_list, second_list):
        # See constraints
        if first_list is None or second_list is None:
            return None
        head = self._add_reverse(first_list.head, second_list.head, 0)
        return MyLinkedList(head)
```

## Unit Test

```python
%%writefile test_add_reverse.py
import unittest


class TestAddReverse(unittest.TestCase):

    def test_add_reverse(self):
        print('Test: Empty list(s)')
        self.assertEqual(MyLinkedList().add_reverse(None, None), None)
        self.assertEqual(MyLinkedList().add_reverse(Node(5), None), None)
        self.assertEqual(MyLinkedList().add_reverse(None, Node(10)), None)

        print('Test: Add values of different lengths')
        # Input 1: 6->5->None
        # Input 2: 9->8->7
        # Result: 5->4->8
        first_list = MyLinkedList(Node(6))
        first_list.append(5)
        second_list = MyLinkedList(Node(9))
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 8])

        print('Test: Add values of same lengths')
        # Input 1: 6->5->4
        # Input 2: 9->8->7
        # Result: 5->4->2->1
        first_head = Node(6)
        first_list = MyLinkedList(first_head)
        first_list.append(5)
        first_list.append(4)
        second_head = Node(9)
        second_list = MyLinkedList(second_head)
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 2, 1])

        print('Success: test_add_reverse')


def main():
    test = TestAddReverse()
    test.test_add_reverse()


if __name__ == '__main__':
    main()
```

    Overwriting test_add_reverse.py

```python
%run -i test_add_reverse.py
```

    Test: Empty list(s)
    Test: Add values of different lengths
    Test: Add values of same lengths
    Success: test_add_reverse
