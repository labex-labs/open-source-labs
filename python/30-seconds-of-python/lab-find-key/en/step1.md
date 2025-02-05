# Find the Key of a Value in a Dictionary

Write a function `find_key(dict, val)` that finds the first key in the provided dictionary that has the given value.

Your function should:

- Take a dictionary `dict` and a value `val` as input.
- Use `dictionary.items()` and `next()` to return the first key that has a value equal to `val`.
- Return the key as output.

```python
def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
find_key(ages, 11) # 'Isabel'
```
