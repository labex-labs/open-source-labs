# Initialize List with Values

Write a function `initialize_list_with_values(n, val=0)` that takes in two parameters:

- `n` (integer) representing the length of the list to be created.
- `val` (integer) representing the value to be used to fill the list. If `val` is not provided, the default value of `0` should be used.

The function should return a list of length `n` filled with the specified value.

```python
def initialize_list_with_values(n, val = 0):
  return [val for x in range(n)]
```

```python
initialize_list_with_values(5, 2) # [2, 2, 2, 2, 2]
```
