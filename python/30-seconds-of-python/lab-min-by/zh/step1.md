# 根据函数找出列表中的最小值

编写一个名为 `min_by(lst, fn)` 的函数，它接受一个列表 `lst` 和一个函数 `fn` 作为参数。该函数应使用提供的函数将列表中的每个元素映射为一个值，然后返回最小值。

```python
def min_by(lst, fn):
  return min(map(fn, lst))
```

```python
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```
