# 最大元素的索引

编写一个函数 `max_element_index(arr)`，该函数接受一个列表 `arr` 作为参数，并返回具有最大值的元素的索引。如果有多个元素具有最大值，则返回第一个出现的元素的索引。

要解决此问题，你可以按以下步骤操作：

1. 使用内置的 `max()` 函数找到列表中的最大值。
2. 使用内置的 `list.index()` 函数找到列表中第一个出现的最大值的索引。
3. 返回该索引。

```python
def max_element_index(arr):
  return arr.index(max(arr))
```

```python
max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4
```
