# 对称差

编写一个函数 `symmetric_difference(a, b)`，它接受两个列表作为参数，并将它们的对称差作为列表返回。该函数不应过滤掉重复值。

要解决此问题，你可以按以下步骤操作：

1. 从每个列表创建一个集合。
2. 对它们中的每一个使用列表推导式，只保留不在另一个先前创建的集合中的值。
3. 连接步骤 2 中获得的两个列表。

```python
def symmetric_difference(a, b):
  (_a, _b) = (set(a), set(b))
  return [item for item in a if item not in _b] + [item for item in b
          if item not in _a]
```

```python
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
```
