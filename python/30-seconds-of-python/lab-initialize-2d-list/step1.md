# Initialize 2D List

Write a function `initialize_2d_list(w, h, val=None)` that initializes a 2D list of given width and height and value. The function should return a list of `h` rows where each row is a list with length `w`, initialized with `val`. If `val` is not provided, the default value should be `None`.

```python
def initialize_2d_list(w, h, val = None):
  return [[val for x in range(w)] for y in range(h)]
```

```python
initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
```
