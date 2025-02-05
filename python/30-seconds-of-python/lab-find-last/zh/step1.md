# 找到最后一个匹配值

编写一个函数 `find_last(lst, fn)`，它接受一个列表 `lst` 和一个测试函数 `fn` 作为参数。该函数应返回 `lst` 中最后一个使 `fn` 返回 `True` 的元素的值。如果没有元素满足测试函数，该函数应返回 `None`。

要解决这个问题，你应该使用列表推导式和 `next()` 以相反的顺序遍历列表，并返回满足测试函数的最后一个元素。

```python
def find_last(lst, fn):
  return next(x for x in lst[::-1] if fn(x))
```

```python
find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
```
