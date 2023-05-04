# Merge Lists

Write a function called `merge(*args, fill_value=None)` that takes in two or more lists as arguments and returns a list of lists. The function should combine elements from each of the input lists based on their positions. If a list is shorter than the longest list, the function should use `fill_value` for the remaining items. If `fill_value` is not provided, it should default to `None`.

Your task is to implement the `merge()` function.

```py
def merge(*args, fill_value = None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
```

```py
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```
