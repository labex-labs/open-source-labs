# Sum List Based on Function

Write a function `sum_by(lst, fn)` that takes a list `lst` and a function `fn` as arguments. The function should map each element of the list to a value using the provided function, and return the sum of the values.

```python
def sum_by(lst, fn):
  return sum(map(fn, lst))
```

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```
