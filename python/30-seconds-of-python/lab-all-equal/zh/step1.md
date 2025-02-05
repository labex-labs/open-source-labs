# 检查列表元素是否相同

编写一个函数 `all_equal(lst)`，它接受一个列表作为参数，如果列表中的所有元素都相同，则返回 `True`，否则返回 `False`。

要解决这个问题，你可以使用以下步骤：

1. 使用 `set()` 来消除列表中的重复元素。
2. 使用 `len()` 检查集合的长度是否为 `1`。
3. 如果集合的长度为 `1`，则返回 `True`。否则，返回 `False`。

```python
def all_equal(lst):
  return len(set(lst)) == 1
```

```python
all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True
```
