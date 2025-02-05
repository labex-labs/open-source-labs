# 列表包含关系

编写一个函数 `is_contained_in(a, b)`，它接受两个列表作为参数，如果列表 `a` 的所有元素都包含在列表 `b` 中（不考虑顺序），则返回 `True`。否则，该函数应返回 `False`。

要解决这个问题，你可以使用以下方法：

1. 遍历列表 `a` 中的每个唯一值。
2. 对于每个值，检查它在列表 `a` 中出现的次数是否比在列表 `b` 中出现的次数多。
3. 如果有任何值在列表 `a` 中出现的次数比在列表 `b` 中多，则返回 `False`。
4. 如果列表 `a` 中的所有值在列表 `b` 中出现的次数至少与它们在列表 `a` 中出现的次数一样多，则返回 `True`。

```python
def is_contained_in(a, b):
  for v in set(a):
    if a.count(v) > b.count(v):
      return False
  return True
```

```python
is_contained_in([1, 4], [2, 4, 1]) # True
```
