# 检查一个列表中的任何值是否包含在另一个列表中

编写一个函数 `includes_any(lst, values)`，它接受两个列表作为参数。该函数应检查 `values` 中的任何元素是否包含在 `lst` 中。如果找到任何一个值，函数应返回 `True`，否则应返回 `False`。

要解决这个问题，你可以使用 `for` 循环遍历 `values` 中的每个值。然后，你可以使用 `in` 运算符检查该值是否包含在 `lst` 中。如果找到一个值，返回 `True`。如果没有找到值，返回 `False`。

```python
def includes_any(lst, values):
  for v in values:
    if v in lst:
      return True
  return False
```

```python
includes_any([1, 2, 3, 4], [2, 9]) # True
includes_any([1, 2, 3, 4], [8, 9]) # False
```
