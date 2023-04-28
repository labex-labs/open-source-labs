# Combine Dictionary Values

## Problem
Write a function `combine_values(*dicts)` that takes two or more dictionaries as arguments and returns a new dictionary that combines the values of the input dictionaries. The function should perform the following steps:

1. Create a new `collections.defaultdict` with `list` as the default value for each key.
2. Loop over the input dictionaries and for each dictionary:
   - Loop over the keys of the dictionary.
   - Append the value of the key to the list of values for that key in the `defaultdict`.
3. Convert the `defaultdict` to a regular dictionary using the `dict()` function.
4. Return the resulting dictionary.

The function should have the following signature:
```python
def combine_values(*dicts):
    pass
```

## Example
```python
d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
```

