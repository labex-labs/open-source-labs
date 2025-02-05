# 列表交集

编写一个函数 `list_intersection(a, b)`，它接受两个列表 `a` 和 `b` 作为输入，并返回一个新列表，其中只包含同时存在于 `a` 和 `b` 中的元素。如果没有共同元素，该函数应返回一个空列表。

```python
def intersection(a, b):
  _a, _b = set(a), set(b)
  return list(_a & _b)
```

```python
intersection([1, 2, 3], [4, 3, 2]) # [2, 3]
```
