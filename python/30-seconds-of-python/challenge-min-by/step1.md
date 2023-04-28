# Find the Minimum Value of a List Based on a Function

## Problem

Write a function called `min_by(lst, fn)` that takes a list `lst` and a function `fn` as arguments. The function should map each element in the list to a value using the provided function, and then return the minimum value.

### Example

```py
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```

In the example above, the `min_by()` function is called with a list of dictionaries and a lambda function that extracts the value of the `'n'` key from each dictionary. The function returns the minimum value of the list, which is `2`.
