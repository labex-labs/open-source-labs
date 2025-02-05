# 根据函数计算列表元素之和

编写一个函数 `sum_by(lst, fn)`，它接受一个列表 `lst` 和一个函数 `fn` 作为参数。该函数应使用提供的函数将列表的每个元素映射到一个值，并返回这些值的总和。

```python
def sum_by(lst, fn):
  return sum(map(fn, lst))
```

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```
