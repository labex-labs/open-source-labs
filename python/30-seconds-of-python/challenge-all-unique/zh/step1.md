# 检查列表函数中的重复项

## 问题

编写一个名为 `has_duplicates(lst)` 的 Python 函数，该函数接受一个列表作为参数，如果列表中有任何重复元素，则返回 `True`，否则返回 `False`。

要解决这个问题，你可以按照以下步骤进行：

1. 将列表转换为集合以删除重复项。
2. 比较集合的长度与原始列表的长度。
3. 如果长度相等，则列表没有重复项，否则有重复项。

## 示例

```python
has_duplicates([1, 2, 3, 4, 5]) # False
has_duplicates([1, 2, 3, 4, 5, 5]) # True
has_duplicates(['apple', 'banana', 'orange', 'banana']) # True
has_duplicates([]) # False
```
