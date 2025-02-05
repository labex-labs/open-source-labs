# 测试列表中是否有某些元素为真值

编写一个函数 `some(lst, fn)`，它接受一个列表 `lst` 和一个函数 `fn` 作为参数。如果函数 `fn` 对列表 `lst` 中的至少一个元素返回 `True`，则该函数应返回 `True`。如果列表中没有元素满足该条件，函数应返回 `False`。如果未提供函数，该函数应使用恒等函数（即返回元素本身的函数）。

```python
def some(lst, fn = lambda x: x):
  return any(map(fn, lst))
```

```python
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True
```
