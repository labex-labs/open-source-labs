# Find All Matching Indexes

## Problem

Write a function `find_index_of_all(lst, fn)` that takes a list `lst` and a testing function `fn` as arguments and returns a list of indexes of all elements in `lst` for which `fn` returns `True`.

### Input

- A list `lst` of integers.
- A testing function `fn` that takes an integer as input and returns a boolean value.

### Output

- A list of integers representing the indexes of all elements in `lst` for which `fn` returns `True`.

## Example

```python
find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
find_index_of_all([1, 2, 3, 4], lambda n: n > 2) # [2, 3]
find_index_of_all([1, 2, 3, 4], lambda n: n < 0) # []
```

### Note

- In the first example, the testing function `lambda n: n % 2 == 1` checks if the integer is odd. The function returns `[0, 2]` because the elements at indexes `0` and `2` of the list `[1, 2, 3, 4]` are odd.
- In the second example, the testing function `lambda n: n > 2` checks if the integer is greater than `2`. The function returns `[2, 3]` because the elements at indexes `2` and `3` of the list `[1, 2, 3, 4]` are greater than `2`.
- In the third example, the testing function `lambda n: n < 0` checks if the integer is negative. The function returns `[]` because there are no negative elements in the list `[1, 2, 3, 4]`.
