# Execute function for each list element in reverse

## Problem

Write a function `for_each_right(itr, fn)` that takes a list `itr` and a function `fn` as arguments. The function should execute `fn` once for each element in `itr`, starting from the last one.

## Example

```py
for_each_right([1, 2, 3], print) # 3 2 1
```

## Constraints

- The function should work for any list and function.
- The function should not modify the original list.
