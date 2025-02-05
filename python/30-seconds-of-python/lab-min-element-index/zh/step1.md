# 最小元素的索引

编写一个函数 `min_element_index(arr)`，它接受一个整数列表 `arr` 作为参数，并返回列表中具有最小值的元素的索引。

要解决这个问题，你可以使用 `min()` 函数来获取列表中的最小值，然后使用 `list.index()` 方法返回其索引。

```python
def min_element_index(arr):
  return arr.index(min(arr))
```

```python
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
```
