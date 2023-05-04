# Symmetric Difference Based on Function

## Problem

Write a function `symmetric_difference_by(a, b, fn)` that takes in two lists `a` and `b`, and a function `fn`. The function should return a new list containing all elements that are in either of the original lists, but not in both, after applying the provided function to each list element of both.

To solve this problem, you can follow these steps:

1. Create a `set` by applying `fn` to each element in every list.
2. Use a list comprehension in combination with `fn` on each of them to only keep values not contained in the previously created set of the other.
3. Concatenate the two lists obtained in step 2.

The function should have the following parameters:

- `a`: a list of elements
- `b`: a list of elements
- `fn`: a function that takes an element and returns a new value

The function should return a new list containing all elements that are in either of the original lists, but not in both, after applying the provided function to each list element of both.

## Example

```python
from math import floor

assert symmetric_difference_by([2.1, 1.2], [2.3, 3.4], floor) == [1.2, 3.4]
```
