# Insertion Sort

## Problem

The problem is to implement insertion sort in Python. Given an unsorted list of elements, the algorithm should sort the list in ascending order. The algorithm works by iterating over the list and inserting each element in its correct position in the sorted part of the list.

The algorithm starts by assuming that the first element in the list is already sorted. It then iterates over the remaining elements in the list, comparing each element to the elements in the sorted part of the list. If the element is smaller than the current element in the sorted part of the list, it is inserted before that element. If the element is larger than all the elements in the sorted part of the list, it is inserted at the end of the sorted part of the list.

## Requirements

To implement insertion sort in Python, the following requirements should be met:

- A naive solution is sufficient.
- Duplicates are allowed.
- The input is not necessarily valid, so the algorithm should handle invalid input gracefully.
- The algorithm should fit in memory.

## Example Usage

The following are some examples of how to use the insertion sort algorithm:

- None -> Exception: If the input is None, an exception should be raised.
- Empty input -> []: If the input is an empty list, the output should also be an empty list.
- One element -> [element]: If the input is a list with only one element, the output should be the same list.
- Two or more elements: If the input is a list with two or more elements, the output should be a sorted list in ascending order.
