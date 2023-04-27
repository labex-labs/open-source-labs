# Find Loop Start

## Problem

Given a singly linked list, we need to find the start of a loop if it exists. A loop is defined as a node in the list that points to a previous node, creating a cycle. If there is no loop, we return None. If there is a loop, we return the node where the loop starts.

## Requirements

To solve this problem, we need to consider the following requirements:

- The linked list is a singly linked list.
- We cannot assume that we are always passed a circular linked list.
- When we find a loop, we return the node where the loop starts.
- We can assume that we already have a linked list class that can be used for this problem.

## Example Usage

Here are some examples of how this function can be used:

- Empty list -> None
- Not a circular linked list -> None
  - One element
  - Two or more elements
- Circular linked list general case
