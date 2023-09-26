# Key of Min Value

Write a function `key_of_min(d)` that takes in a dictionary `d` as its argument and returns the key of the minimum value in the dictionary.

To solve this problem, you can use the built-in `min()` function with the `key` parameter set to `dict.get()`. This will return the key of the minimum value in the dictionary.

```python
def key_of_min(d):
  return min(d, key = d.get)
```

```python
key_of_min({'a':4, 'b':0, 'c':13}) # b
```
