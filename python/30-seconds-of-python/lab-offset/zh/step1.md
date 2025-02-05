# 偏移列表元素

编写一个函数 `offset(lst, offset)`，它接受一个列表 `lst` 和一个整数 `offset` 作为参数，并返回一个新列表，其中指定数量的元素被移动到了列表末尾。如果 `offset` 是正数，则将前 `offset` 个元素移动到列表末尾。如果 `offset` 是负数，则将最后 `offset` 个元素移动到列表开头。

```python
def offset(lst, offset):
  return lst[offset:] + lst[:offset]
```

```python
offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]
```
