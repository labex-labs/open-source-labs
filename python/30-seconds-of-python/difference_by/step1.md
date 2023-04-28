# List Difference Based on Function

## Problem
Create a function called `difference_by(a, b, fn)` that takes in three parameters:
- `a`: a list of elements
- `b`: a list of elements
- `fn`: a function that will be applied to each element in both lists

The function should return a list of elements that are in list `a` but not in list `b`, after applying the provided function `fn` to each element in both lists.

To solve this problem, you can follow these steps:
1. Create a `set`, using `map()` to apply `fn` to each element in `b`.
2. Use a list comprehension in combination with `fn` on `a` to only keep values not contained in the previously created set, `_b`.

## Example
```py
difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])
# [ { x: 2 } ]
```

