# 列表差异

编写一个名为 `list_difference(a, b)` 的 Python 函数，该函数接受两个列表作为参数，并返回它们之间的差异。该函数不应过滤掉重复值。要解决此问题，你可以按以下步骤操作：

1. 从第二个列表 `b` 创建一个集合。
2. 对第一个列表 `a` 使用列表推导式，只保留不在先前创建的集合 `_b` 中的值。
3. 返回结果列表。

```python
def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]
```

```python
difference([1, 2, 3], [1, 2, 4]) # [3]
```
