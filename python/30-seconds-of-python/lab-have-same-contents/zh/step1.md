# 检查两个列表是否具有相同的内容

编写一个函数 `have_same_contents(a, b)`，它接受两个列表作为参数，如果两个列表具有相同的内容，则返回 `True`，否则返回 `False`。该函数应检查两个列表是否包含相同的元素，而不考虑它们的顺序。

要解决这个问题，你可以按照以下步骤进行：

1. 对两个列表的组合使用 `set()` 来找到唯一值。
2. 使用 `for` 循环遍历它们，比较每个列表中每个唯一值的 `count()`。
3. 如果任何元素的计数不匹配，则返回 `False`，否则返回 `True`。

```python
def have_same_contents(a, b):
  for v in set(a + b):
    if a.count(v)!= b.count(v):
      return False
  return True
```

```python
have_same_contents([1, 2, 4], [2, 4, 1]) # True
```
