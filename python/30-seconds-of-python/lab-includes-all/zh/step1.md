# 检查一个列表是否包含所有值

编写一个名为 `includes_all(lst, values)` 的函数，该函数接受两个列表作为参数。该函数应检查 `values` 列表中的所有值是否都包含在 `lst` 列表中。如果所有值都包含在内，函数应返回 `True`。如果有任何值未包含在内，函数应返回 `False`。

要解决此问题，你应该：

1. 使用 `for` 循环遍历 `values` 列表中的每个值。
2. 使用 `in` 运算符检查当前值是否包含在 `lst` 列表中。
3. 如果该值未包含在内，则返回 `False`。
4. 如果所有值都包含在内，则返回 `True`。

```python
def includes_all(lst, values):
  for v in values:
    if v not in lst:
      return False
  return True
```

```python
includes_all([1, 2, 3, 4], [1, 4]) # True
includes_all([1, 2, 3, 4], [1, 5]) # False
```
