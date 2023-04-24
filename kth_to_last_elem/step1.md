# Kth To Last Elem

## Problem

Given a non-circular, singly linked list, the task is to find the kth to last element of the list. If k is 0, the last element should be returned. If k is greater than or equal to the length of the linked list, None should be returned. No additional data structures can be used, and it is assumed that a linked list class is already available.

## Requirements

To solve this problem, the following requirements must be met:

- The linked list is non-circular and singly linked.
- k is a valid integer.
- If k is 0, the last element should be returned.
- If k is greater than or equal to the length of the linked list, None should be returned.
- No additional data structures can be used.
- A linked list class is already available.

## Example Usage

The following scenarios can be used to test the solution:

- An empty list should return None.
- If k is greater than or equal to the length of the linked list, None should be returned.
- If the linked list has only one element and k is 0, the element should be returned.
- For a general case with many elements, where k is less than the length of the linked list, the kth to last element should be returned.
