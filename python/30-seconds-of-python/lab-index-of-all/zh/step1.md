# 值的所有索引

编写一个名为 `index_of_all(lst, value)` 的 Python 函数，该函数接受一个列表 `lst` 和一个值 `value` 作为参数，并返回 `value` 在 `lst` 中所有出现位置的索引列表。

要解决这个问题，你可以使用 `enumerate()` 和列表推导式来检查每个元素是否等于 `value`，并将 `i` 添加到结果中。

```python
def index_of_all(lst, value):
  return [i for i, x in enumerate(lst) if x == value]
```

```python
index_of_all([1, 2, 1, 4, 5, 1], 1) # [0, 2, 5]
index_of_all([1, 2, 3, 4], 6) # []
```
