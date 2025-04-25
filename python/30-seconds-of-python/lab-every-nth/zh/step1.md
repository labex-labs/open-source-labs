# 列表中的每隔第 n 个元素

编写一个函数 `every_nth(lst, nth)`，它接受一个列表 `lst` 和一个整数 `nth` 作为参数，并返回一个新列表，该新列表包含原始列表中的每隔第 `n` 个元素。

```python
def every_nth(lst, nth):
  return lst[nth - 1::nth]
```

```python
every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]
```
