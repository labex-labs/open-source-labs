# Sum List Based on Function

## Problem

Write a function `sum_by(lst, fn)` that takes a list `lst` and a function `fn` as arguments. The function should map each element of the list to a value using the provided function, and return the sum of the values.

## Example

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```

In the example above, the `sum_by()` function takes a list of dictionaries and a lambda function that extracts the value of the `'n'` key from each dictionary. The function maps each dictionary to its `'n'` value and returns the sum of the values, which is `20`.
