# List Intersection Based on Function

## Problem

Write a function `intersection_by(a, b, fn)` that takes in two lists `a` and `b`, and a function `fn`. The function should return a list of elements that exist in both lists, after applying the provided function to each list element of both.

### Input

- Two lists `a` and `b` (1 <= len(a), len(b) <= 1000)
- A function `fn` that takes in one argument and returns a value

### Output

- A list of elements that exist in both lists, after applying the provided function to each list element of both.

## Example

```python
intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```

### Note

In the example above, the function `floor()` is applied to each element in both lists. The resulting sets are `{2, 3}` and `{2, 1}`. The intersection of these sets is `{2}`, which is then returned as a list.
