# Check if Key Exists in Dictionary

Write a function `key_in_dict(d, key)` that takes a dictionary `d` and a key `key` as arguments and returns `True` if the key exists in the dictionary, `False` otherwise.

```py
def key_in_dict(d, key):
  return (key in d)
```

```py
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
```
