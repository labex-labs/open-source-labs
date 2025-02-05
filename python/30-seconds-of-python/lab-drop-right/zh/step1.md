# 从右侧删除列表元素

编写一个函数 `drop_right(a, n = 1)`，它接受一个列表 `a` 和一个可选整数 `n`，并返回一个新列表，其中从列表 `a` 的右端删除了 `n` 个元素。如果未提供 `n`，则该函数应仅从列表中删除最后一个元素。

```python
def drop_right(a, n = 1):
  return a[:-n]
```

```python
drop_right([1, 2, 3]) # [1, 2]
drop_right([1, 2, 3], 2) # [1]
drop_right([1, 2, 3], 42) # []
```
