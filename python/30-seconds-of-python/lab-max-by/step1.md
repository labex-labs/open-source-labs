# Find Maximum List Value Based on Function

Write a function `max_by(lst, fn)` that takes a list `lst` and a function `fn` as arguments. The function should map each element in `lst` to a value using the provided function `fn`, and then return the maximum value.

```python
def max_by(lst, fn):
  return max(map(fn, lst))
```

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```
