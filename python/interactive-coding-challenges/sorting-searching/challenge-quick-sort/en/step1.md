# Quick Sort

## Problem

Implement Quick Sort algorithm in Python. The algorithm should take an unsorted list as input and return a sorted list. The algorithm should work for lists of any size, including empty lists and lists with duplicate elements. The algorithm should also handle invalid input gracefully.

The Quick Sort algorithm works as follows:

1. Choose a pivot element from the list.
2. Partition the list into two sub-lists: one with elements less than the pivot, and one with elements greater than the pivot.
3. Recursively apply the Quick Sort algorithm to the sub-lists.
4. Concatenate the sorted sub-lists with the pivot element in the middle.

## Requirements

To implement Quick Sort algorithm in Python, the following requirements should be met:

- The algorithm should not be an in-place solution.
- The algorithm should handle duplicate elements in the list.
- The algorithm should handle invalid input, such as None or non-list input.
- The algorithm should be able to handle lists of any size, including empty lists.

## Example Usage

The following are some examples of how to use the Quick Sort algorithm in Python:

- None -> Exception

```python
quick_sort(None)
```

- Empty input -> []

```python
quick_sort([])
```

- One element -> [element]

```python
quick_sort([5])
```

- Two or more elements

```python
quick_sort([5, 2, 8, 3, 1, 9])
```
