# For and tuples

You can iterate with multiple iteration variables.

```python
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    # Loops with x = 1, y = 4
    #            x = 10, y = 40
    #            x = 23, y = 14
    #            ...
```

When using multiple variables, each tuple is _unpacked_ into a set of iteration variables. The number of variables must match the number of items in each tuple.
