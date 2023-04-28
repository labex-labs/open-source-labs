# Key of Min Value

## Problem

Write a function `key_of_min(d)` that takes in a dictionary `d` as its argument and returns the key of the minimum value in the dictionary.

To solve this problem, you can use the built-in `min()` function with the `key` parameter set to `dict.get()`. This will return the key of the minimum value in the dictionary.

## Example

```python
key_of_min({'a':4, 'b':0, 'c':13}) # 'b'
```

In this example, the dictionary `{'a':4, 'b':0, 'c':13}` is passed as an argument to the `key_of_min()` function. The function returns the key `'b'`, which corresponds to the minimum value in the dictionary.

