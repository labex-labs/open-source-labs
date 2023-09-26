# Lists to Dictionary

Write a function `to_dictionary(keys, values)` that takes two lists as input and returns a dictionary where the elements of the first list serve as the keys and the elements of the second list serve as the values. The function should use `zip()` in combination with `dict()` to combine the values of the two lists into a dictionary. The function should return `None` if the length of the two lists is not equal.

```python
def to_dictionary(keys, values):
  return dict(zip(keys, values))
```

```python
to_dictionary(['a', 'b'], [1, 2]) # { a: 1, b: 2 }
```
