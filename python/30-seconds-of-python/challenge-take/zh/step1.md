# 移除列表元素

## 问题

编写一个函数 `take(itr, n=1)`，它接受一个列表 `itr` 和一个整数 `n` 作为参数，并返回一个新列表，该列表从原列表开头移除了 `n` 个元素。如果 `n` 大于列表的长度，则返回原列表。

## 示例

```python
take([1, 2, 3], 1) # [2, 3]
take([1, 2, 3], 2) # [3]
take([1, 2, 3], 3) # []
take([1, 2, 3], 4) # []
```
