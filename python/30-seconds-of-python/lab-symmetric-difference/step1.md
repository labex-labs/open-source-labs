# Symmetric Difference

Write a function `symmetric_difference(a, b)` that takes two lists as arguments and returns their symmetric difference as a list. The function should not filter out duplicate values.

To solve this problem, you can follow these steps:

1. Create a set from each list.
2. Use a list comprehension on each of them to only keep values not contained in the previously created set of the other.
3. Concatenate the two lists obtained in step 2.

```py
def symmetric_difference(a, b):
  (_a, _b) = (set(a), set(b))
  return [item for item in a if item not in _b] + [item for item in b
          if item not in _a]
```

```py
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
```
