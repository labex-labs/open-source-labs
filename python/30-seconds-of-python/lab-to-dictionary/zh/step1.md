# 列表转字典

编写一个函数 `to_dictionary(keys, values)`，该函数接受两个列表作为输入，并返回一个字典，其中第一个列表的元素作为键，第二个列表的元素作为值。该函数应使用 `zip()` 并结合 `dict()` 将两个列表的值组合成一个字典。如果两个列表的长度不相等，该函数应返回 `None`。

```python
def to_dictionary(keys, values):
  return dict(zip(keys, values))
```

```python
to_dictionary(['a', 'b'], [1, 2]) # { a: 1, b: 2 }
```
