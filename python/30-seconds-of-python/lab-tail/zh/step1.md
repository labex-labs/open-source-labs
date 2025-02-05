# 列表尾部

编写一个函数 `tail(lst)`，它接受一个列表作为参数，并返回该列表中除第一个元素之外的所有元素。如果列表只包含一个元素，则返回整个列表。

```python
def tail(lst):
  return lst[1:] if len(lst) > 1 else lst
```

```python
tail([1, 2, 3]) # [2, 3]
tail([1]) # [1]
```
