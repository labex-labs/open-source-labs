# Solutions

This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Find the kth to last element of a linked list.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume this is a non-circular, singly linked list?
  - Yes
- Can we assume k is a valid integer?
  - Yes
- If k = 0, does this return the last element?
  - Yes
- What happens if k is greater than or equal to the length of the linked list?
  - Return None
- Can you use additional data structures?
  - No
- Can we assume we already have a linked list class that can be used for this problem?
  - Yes

## Test Cases

- Empty list -> None
- k is >= the length of the linked list -> None
- One element, k = 0 -> element
- General case with many elements, k < length of linked list

## Algorithm

- Setup two pointers, fast and slow
- Give fast a headstart, incrementing it once if k = 1, twice if k = 2, ...
- Increment both pointers until fast reaches the end
- Return the value of slow

Complexity:

- Time: O(n)
- Space: O(1)

## Code

```python
%run ../linked_list/linked_list.py
```

```python
class MyLinkedList(LinkedList):

    def kth_to_last_elem(self, k):
        if self.head is None:
            return None
        fast = self.head
        slow = self.head

        # Give fast a headstart, incrementing it
        # once for k = 1, twice for k = 2, etc
        for _ in range(k):
            fast = fast.next
            # If k >= num elements, return None
            if fast is None:
                return None

        # Increment both pointers until fast reaches the end
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.data
```

## Unit Test

```python
%%writefile test_kth_to_last_elem.py
import unittest


class Test(unittest.TestCase):

    def test_kth_to_last_elem(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        self.assertEqual(linked_list.kth_to_last_elem(0), None)

        print('Test: k >= len(list)')
        self.assertEqual(linked_list.kth_to_last_elem(100), None)

        print('Test: One element, k = 0')
        head = Node(2)
        linked_list = MyLinkedList(head)
        self.assertEqual(linked_list.kth_to_last_elem(0), 2)

        print('Test: General case')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(5)
        linked_list.insert_to_front(7)
        self.assertEqual(linked_list.kth_to_last_elem(2), 3)

        print('Success: test_kth_to_last_elem')


def main():
    test = Test()
    test.test_kth_to_last_elem()


if __name__ == '__main__':
    main()
```

    Overwriting test_kth_to_last_elem.py

```python
%run -i test_kth_to_last_elem.py
```

    Test: Empty list
    Test: k >= len(list)
    Test: One element, k = 0
    Test: General case
    Success: test_kth_to_last_elem
