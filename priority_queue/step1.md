# Priority Queue

## Problem

Implement a priority queue backed by an array. The priority queue should support the following methods:

- `insert`: insert a new element into the priority queue
- `extract_min`: remove and return the minimum element from the priority queue
- `decrease_key`: decrease the key of a given element in the priority queue

## Requirements

To implement the priority queue, we need to meet the following requirements:

- The methods supported by the priority queue should be `insert`, `extract_min`, and `decrease_key`.
- There won't be any duplicate keys in the priority queue.
- We don't need to validate inputs.
- The priority queue should fit into memory.

## Example Usage

Here are some examples of how to use the priority queue methods:

### insert

- `insert` general case: insert a new node into the priority queue.

### extract_min

- `extract_min` from an empty list: return None.
- `extract_min` general case: remove and return the minimum node from the priority queue.

### decrease_key

- `decrease_key` an invalid key: return None.
- `decrease_key` general case: decrease the key of a given node in the priority queue.
