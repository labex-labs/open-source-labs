# 检查列表中的重复项

编写一个名为 `has_duplicates(lst)` 的 Python 函数，该函数接受一个列表作为参数，如果列表包含任何重复项，则返回 `True`，否则返回 `False`。

要解决此问题，你可以使用以下步骤：

1. 使用 `set()` 函数从列表中删除重复项。
2. 比较原始列表的长度和集合的长度。如果它们相同，则没有重复项。如果它们不同，则有重复项。

```python
def has_duplicates(lst):
  return len(lst)!= len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x) # True
has_duplicates(y) # False
```
