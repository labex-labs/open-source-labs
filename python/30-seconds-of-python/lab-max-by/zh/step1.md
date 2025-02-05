# 根据函数查找列表中的最大值

编写一个函数 `max_by(lst, fn)`，它接受一个列表 `lst` 和一个函数 `fn` 作为参数。该函数应使用提供的函数 `fn` 将 `lst` 中的每个元素映射到一个值，然后返回最大值。

```python
def max_by(lst, fn):
  return max(map(fn, lst))
```

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```
