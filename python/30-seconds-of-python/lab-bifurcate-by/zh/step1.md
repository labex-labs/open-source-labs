# 根据函数对列表进行二分

编写一个函数 `bifurcate_by(lst, fn)`，它接受一个列表 `lst` 和一个过滤函数 `fn` 作为参数。该函数应根据过滤函数的结果将列表拆分为两组。如果过滤函数对某个元素返回真值，则应将其添加到第一组。否则，应将其添加到第二组。

你的函数应返回一个包含两个列表的列表，其中第一个列表包含过滤函数返回真值的所有元素，第二个列表包含过滤函数返回假值的所有元素。

使用列表推导式根据 `fn` 对每个元素返回的值将元素添加到相应的组中。

```python
def bifurcate_by(lst, fn):
  return [
    [x for x in lst if fn(x)],
    [x for x in lst if not fn(x)]
  ]
```

```python
bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```
