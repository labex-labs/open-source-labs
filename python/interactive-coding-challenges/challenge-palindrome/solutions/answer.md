# Solution Notebook

This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Determine if a linked list is a palindrome.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume this is a non-circular, singly linked list?
  - Yes
- Is a single character or number a palindrome?
  - No
- Can we assume we already have a linked list class that can be used for this problem?
  - Yes
- Can we use additional data structures?
  - Yes
- Can we assume this fits in memory?
  - Yes

## Test Cases

- Empty list -> False
- Single element list -> False
- Two or more element list, not a palindrome -> False
- General case: Palindrome with even length -> True
- General case: Palindrome with odd length -> True

## Algorithm

- Reverse the linked list
  - Iterate through the current linked list
    - Insert to front the current node into a new linked list
- Compare the reversed list with the original list
  - Only need to compare the first half

Complexity:

- Time: O(n)
- Space: O(n)

Note:

- We could also do this iteratively, using a stack to effectively reverse the first half of the string.

## Code

```python
%run ../linked_list/linked_list.py
```

```python
from __future__ import division


class MyLinkedList(LinkedList):

    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return False
        curr = self.head
        reversed_list = MyLinkedList()
        length = 0

        # Reverse the linked list
        while curr is not None:
            reversed_list.insert_to_front(curr.data)
            length += 1
            curr = curr.next

        # Compare the reversed list with the original list
        # Only need to compare the first half
        iterations = length // 2
        curr = self.head
        curr_reversed = reversed_list.head
        for _ in range(iterations):
            if curr.data != curr_reversed.data:
                return False
            curr = curr.next
            curr_reversed = curr_reversed.next
        return True
```

## Unit Test

```python
%%writefile test_palindrome.py
import unittest


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        print('Test: Empty list')
        linked_list = MyLinkedList()
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: Single element list')
        head = Node(1)
        linked_list = MyLinkedList(head)
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: Two element list, not a palindrome')
        linked_list.append(2)
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = MyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        self.assertEqual(linked_list.is_palindrome(), True)

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = MyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        self.assertEqual(linked_list.is_palindrome(), True)

        print('Success: test_palindrome')


def main():
    test = TestPalindrome()
    test.test_palindrome()


if __name__ == '__main__':
    main()
```

    Overwriting test_palindrome.py

```python
%run -i test_palindrome.py
```

    Test: Empty list
    Test: Single element list
    Test: Two element list, not a palindrome
    Test: General case: Palindrome with even length
    Test: General case: Palindrome with odd length
    Success: test_palindrome
