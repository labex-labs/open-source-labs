# Linked List

## Problem

Implement a linked list with the following methods:

- insert(value): inserts a new node with the given value at the front of the list
- append(value): inserts a new node with the given value at the end of the list
- find(value): returns the first node in the list with the given value, or None if no such node exists
- delete(value): removes the first node in the list with the given value, or does nothing if no such node exists
- length(): returns the number of nodes in the list
- print(): prints the values of all nodes in the list, separated by spaces

## Requirements

The linked list implementation should meet the following requirements:

- The linked list is non-circular and singly linked.
- The implementation only keeps track of the head of the list, not the tail.
- None values cannot be inserted into the list.

## Example Usage

### Insert to Front

- Insert a None: Raises an error as None values cannot be inserted into the list.
- Insert in an empty list: Inserts the value as the first node in the list.
- Insert in a list with one element or more elements: Inserts the value as the first node in the list, shifting the existing nodes to the right.

### Append

- Append a None: Raises an error as None values cannot be inserted into the list.
- Append in an empty list: Inserts the value as the first node in the list.
- Append in a list with one element or more elements: Inserts the value as the last node in the list, updating the reference of the previous last node to point to the new node.

### Find

- Find a None: Returns None as None values cannot be found in the list.
- Find in an empty list: Returns None as there are no nodes in the list.
- Find in a list with one element or more matching elements: Returns the first node in the list with the given value.
- Find in a list with no matches: Returns None as there are no nodes in the list with the given value.

### Delete

- Delete a None: Does nothing as None values cannot be deleted from the list.
- Delete in an empty list: Does nothing as there are no nodes in the list.
- Delete in a list with one element or more matching elements: Removes the first node in the list with the given value, shifting the existing nodes to the left.
- Delete in a list with no matches: Does nothing as there are no nodes in the list with the given value.

### Length

- Length of zero or more elements: Returns the number of nodes in the list.

### Print

- Print an empty list: Prints nothing.
- Print a list with one or more elements: Prints the values of all nodes in the list, separated by spaces.
