# Find the Minimum Value of a List Based on a Function

Write a function called `min_by(lst, fn)` that takes a list `lst` and a function `fn` as arguments. The function should map each element in the list to a value using the provided function, and then return the minimum value.

```python
def min_by(lst, fn):
  return min(map(fn, lst))
```

```python
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```
