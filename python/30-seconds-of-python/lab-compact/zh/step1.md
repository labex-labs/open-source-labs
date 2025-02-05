# 压缩列表

编写一个函数 `compact(lst)`，它接受一个列表作为参数，并返回一个移除了所有虚假值的新列表。虚假值包括 `False`、`None`、`0` 和 `""`。

要解决这个问题，你可以使用 `filter()` 函数从列表中过滤掉虚假值。

```python
def compact(lst):
  return list(filter(None, lst))
```

```python
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```
