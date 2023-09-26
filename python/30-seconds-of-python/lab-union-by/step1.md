# List Union Based on Function

Write a function `union_by(a, b, fn)` that takes in two lists `a` and `b`, and a function `fn`. The function should return a list that contains every element that exists in any of the two lists once, after applying the provided function to each element of both.

To solve this problem, you can follow these steps:

1. Create a `set` by applying `fn` to each element in `a`.
2. Use a list comprehension in combination with `fn` on `b` to only keep values not contained in the previously created set, `_a`.
3. Finally, create a `set` from the previous result and `a` and transform it into a `list`.

The function should have the following input parameters:

- `a`: a list of elements
- `b`: a list of elements
- `fn`: a function that takes an element and returns a value

The function should return a list of elements.

```python
def union_by(a, b, fn):
  _a = set(map(fn, a))
  return list(set(a + [item for item in b if fn(item) not in _a]))
```

```python
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```
