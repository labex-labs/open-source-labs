# Stack

## Problem

Implement a stack using a linked list in Python, with the following methods:

- push: adds an element to the top of the stack
- pop: removes and returns the element at the top of the stack. If the stack is empty, return None.
- peek: returns the element at the top of the stack without removing it. If the stack is empty, return None.
- is_empty: returns True if the stack is empty, False otherwise.

## Requirements

The following requirements should be met:

- When popping an empty stack, return None.
- The implementation should use a linked list.
- The implementation should be in Python.
- The implementation should include the four methods: push, pop, peek, and is_empty.

## Example Usage

### Push

- Push to empty stack: stack.push(1)
- Push to non-empty stack: stack.push(2)

### Pop

- Pop on empty stack: stack.pop() -> None
- Pop on single element stack: stack.pop() -> 1
- Pop on multiple element stack: stack.pop() -> 2

### Peek

- Peek on empty stack: stack.peek() -> None
- Peek on one or more element stack: stack.peek() -> 2

### Is Empty

- Is empty on empty stack: stack.is_empty() -> True
- Is empty on one or more element stack: stack.is_empty() -> False
