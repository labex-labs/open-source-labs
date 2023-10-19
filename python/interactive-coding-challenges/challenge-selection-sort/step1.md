# Selection Sort

## Problem

Implement selection sort in Python. The algorithm should take a list of integers as input and return the sorted list. The algorithm should work as follows:

1. Find the minimum element in the unsorted part of the list.
2. Swap it with the first element of the unsorted part of the list.
3. Move the boundary of the sorted part of the list one element to the right.

Repeat steps 1-3 until the entire list is sorted.

## Requirements

To implement selection sort in Python, the following requirements must be met:

- The algorithm should take a list of integers as input.
- The algorithm should return a sorted list of integers.
- The algorithm should be implemented using the selection sort algorithm.
- The algorithm should work for lists of any length.
- The algorithm should handle duplicate elements in the list.
- The input list may not be sorted.
- The input list may contain invalid data, such as non-integer values.
- The algorithm should be memory-efficient and not use excessive memory.

## Example Usage

The following examples demonstrate the usage of the selection sort algorithm:

- `selection_sort([])` returns `[]`
- `selection_sort([1])` returns `[1]`
- `selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])` returns `[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]`
