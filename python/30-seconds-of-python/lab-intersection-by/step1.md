# List Intersection Based on Function

Write a function `intersection_by(a, b, fn)` that takes in two lists `a` and `b`, and a function `fn`. The function should return a list of elements that exist in both lists, after applying the provided function to each list element of both.

### Input

- Two lists `a` and `b` (1 <= len(a), len(b) <= 1000)
- A function `fn` that takes in one argument and returns a value

### Output

- A list of elements that exist in both lists, after applying the provided function to each list element of both.

```py
def intersection_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]
```

```py
from math import floor

intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```
