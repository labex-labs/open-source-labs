# 列表相似度

编写一个函数 `similarity(a, b)`，它接受两个列表 `a` 和 `b` 作为参数，并返回一个新列表，该新列表只包含同时存在于 `a` 和 `b` 中的元素。

为了解决这个问题，我们可以使用列表推导式来遍历 `a` 的元素，并检查它们是否存在于 `b` 中。如果一个元素同时存在于两个列表中，我们就将其添加到一个新列表中。

```python
def similarity(a, b):
  return [item for item in a if item in b]
```

```python
similarity([1, 2, 3], [1, 2, 4]) # [1, 2]
```
