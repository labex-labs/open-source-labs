# Set Of Stacks

## Problem

Implement a SetOfStacks class that wraps a list of stacks, where each stack is bound by a capacity. The class should have the following functionalities:

- Push an element onto the top of the last stack in the list. If the last stack is full, create a new stack and add the element to the new stack.
- Pop the top element from the last stack in the list. If the last stack is empty, remove it from the list and pop the top element from the new last stack in the list. If the list is empty, return None.
- Pop an element from a specific stack in the list. If the stack is empty, remove it from the list. If the list is empty, return None.

## Requirements

The SetOfStacks class should meet the following requirements:

- The class should use an existing stack class.
- All stacks in the list should be bound by the same capacity.
- If a stack becomes full, a new stack should be created automatically to store additional elements.
- If a stack becomes empty, it should be removed from the list.
- If we pop on an empty stack, the method should return None.
- The implementation should fit in memory.

## Example Usage

The SetOfStacks class can be used in the following scenarios:

- Push and pop on an empty stack.
- Push and pop on a non-empty stack.
- Push on a capacity stack to create a new one.
- Pop on a stack to destroy it.
