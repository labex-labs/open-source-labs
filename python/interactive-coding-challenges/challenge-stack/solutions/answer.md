# Solution Notebook

This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Implement a stack with push, pop, peek, and is_empty methods using a linked list.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)
- [Pythonic-Code](#Pythonic-Code)

## Constraints

- If we pop on an empty stack, do we return None?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

### Push

- Push to empty stack
- Push to non-empty stack

### Pop

- Pop on empty stack
- Pop on single element stack
- Pop on multiple element stack

### Peek

- Peek on empty stack
- Peek on one or more element stack

### Is Empty

- Is empty on empty stack
- Is empty on one or more element stack

## Algorithm

### Push

- Create new node with value
- Set node's next to top
- Set top to node

Complexity:

- Time: O(1)
- Space: O(1)

### Pop

- If stack is empty, return None
- Else
  - Save top's value
  - Set top to top.next
  - Return saved value

Complexity:

- Time: O(1)
- Space: O(1)

### Peek

- If stack is empty, return None
- Else return top's value

Complexity:

- Time: O(1)
- Space: O(1)

### Is Empty

- If peek has a value, return False
- Else return True

Complexity:

- Time: O(1)
- Space: O(1)

## Code

```python
%%writefile stack.py
class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.peek() is None
```

    Overwriting stack.py

```python
%run stack.py
```

## Unit Test

```python
%%writefile test_stack.py
import unittest


class TestStack(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Empty stack')
        stack = Stack()
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.pop(), None)

        print('Test: One element')
        top = Node(5)
        stack = Stack(top)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.peek(), None)

        print('Test: More than one element')
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.is_empty(), True)

        print('Success: test_end_to_end')


def main():
    test = TestStack()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
```

    Overwriting test_stack.py

```python
%run -i test_stack.py
```

    Test: Empty stack
    Test: One element
    Test: More than one element
    Success: test_end_to_end

## Pythonic-Code

Source: https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks

```txt
5.1.1. Using Lists as Stacks
The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index. For example:

>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```
