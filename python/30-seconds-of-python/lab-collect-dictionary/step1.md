# Invert a Dictionary

Write a function `invert_dictionary(obj)` that takes a dictionary `obj` as input and returns a new dictionary with the keys and values inverted. The input dictionary will have non-unique hashable values. If two or more keys have the same value, the function should append the keys to a list in the output dictionary.

To solve this problem, you can follow these steps:

1. Create a `collections.defaultdict` with `list` as the default value for each key.
2. Use `dictionary.items()` in combination with a loop to map the values of the dictionary to keys using `dict.append()`.
3. Use `dict()` to convert the `collections.defaultdict` to a regular dictionary.

Function signature: `def invert_dictionary(obj: dict) -> dict:`

```python
from collections import defaultdict

def collect_dictionary(obj):
  inv_obj = defaultdict(list)
  for key, value in obj.items():
    inv_obj[value].append(key)
  return dict(inv_obj)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
collect_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```
