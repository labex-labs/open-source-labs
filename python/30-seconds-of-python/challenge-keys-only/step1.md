# Dictionary Keys

## Problem

Write a function `keys_only(flat_dict)` that takes a flat dictionary as input and returns a list of all its keys.

To solve this problem, you can follow these steps:

1. Use `dict.keys()` to return the keys in the given dictionary.
2. Return a `list()` of the previous result.

## Example

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```
