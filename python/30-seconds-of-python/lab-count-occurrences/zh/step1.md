# 统计出现次数

编写一个函数 `count_occurrences(lst, val)`，它接受一个列表 `lst` 和一个值 `val` 作为参数，并返回 `val` 在 `lst` 中出现的次数。你的函数应该使用内置的 `list.count()` 方法来统计出现次数。

```python
def count_occurrences(lst, val):
  return lst.count(val)
```

```python
count_occurrences([1, 1, 2, 1, 2, 3], 1) # 3
```
