# Invert a Dictionary

## Problem

Write a Python function called `invert_dictionary(obj)` that takes a dictionary `obj` as an argument and returns a new dictionary with the keys and values inverted. The input dictionary `obj` will have unique hashable values. The output dictionary should have the same keys as the input dictionary, but the values should be the keys from the input dictionary.

You should use `dictionary.items()` in combination with a list comprehension to create the new dictionary.

## Example

```py
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
```
