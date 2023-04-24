# Min Heap

## Problem

Implement a min heap with the following methods:

- `extract_min()`: removes and returns the minimum value in the heap
- `insert(value)`: inserts a new value into the heap while maintaining the heap property

## Requirements

The implementation should meet the following requirements:

- The inputs are integers
- The implementation should fit in memory

## Example Usage

Consider the following min heap:

```txt
          _5_
        /     \
       20     15
      / \    /  \
     22  40 25
```

- `extract_min()`: removes and returns the minimum value in the heap, which is 5. The resulting heap is:

```txt
          _15_
        /      \
       20      25
      / \     /  \
     22  40 
```

- `insert(2)`: inserts the value 2 into the heap while maintaining the heap property. The resulting heap is:

```txt
          _2_
        /     \
       20      5
      / \     / \
     22  40  25  15
```
