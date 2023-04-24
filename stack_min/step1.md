# Stack Min

## Problem

The problem is to implement a stack with push, pop, and min methods running O(1) time. The push method adds an element to the collection, the pop method removes the most recently added element that was not yet removed, and the min method returns the minimum element in the stack. All three methods should run in constant time, O(1).

## Requirements

To solve this problem, we need to consider the following requirements:

- The stack contains only integers.
- The input values for push are valid.
- If we call the min method on an empty stack, we should return sys.maxsize.
- We can assume that we already have a stack class that can be used for this problem.
- We can assume that the stack fits in memory.

## Example Usage

We can test our implementation with the following scenarios:

- Push/pop on an empty stack.
- Push/pop on a non-empty stack.
- Min on an empty stack.
- Min on a non-empty stack.
