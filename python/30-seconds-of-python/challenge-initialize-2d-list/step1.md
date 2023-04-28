# Initialize 2D List

## Problem

Write a function `initialize_2d_list(w, h, val=None)` that initializes a 2D list of given width and height and value. The function should return a list of `h` rows where each row is a list with length `w`, initialized with `val`. If `val` is not provided, the default value should be `None`.

## Example

```py
initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
initialize_2d_list(3, 3, "x") # [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
initialize_2d_list(2, 3) # [[None, None], [None, None], [None, None]]
```

