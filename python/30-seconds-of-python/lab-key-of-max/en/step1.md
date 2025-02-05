# Key of Max Value

Write a function `key_of_max(d)` that takes a dictionary `d` as an argument and returns the key of the maximum value in the dictionary. If there are multiple keys with the same maximum value, return any one of them.

To solve this problem, you can use the `max()` function with the `key` parameter set to `dict.get()`. This will return the key of the maximum value in the dictionary.

```python
def key_of_max(d):
  return max(d, key = d.get)
```

```python
key_of_max({'a':4, 'b':0, 'c':13}) # c
```
