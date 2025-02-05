# 对列表进行二分

编写一个函数 `bifurcate(lst, filter)`，它接受一个列表 `lst` 和一个筛选条件 `filter` 作为输入，并返回一个包含两个列表的列表。第一个列表应包含 `lst` 中通过筛选条件的元素，第二个列表应包含未通过筛选条件的元素。

要实现这个函数，你可以使用列表推导式和 `zip()` 函数。`zip()` 函数接受两个或更多列表作为输入，并返回一个元组列表，其中每个元组包含来自每个列表的对应元素。例如，`zip([1, 2, 3], [4, 5, 6])` 返回 `[(1, 4), (2, 5), (3, 6)]`。

你可以使用这个函数同时遍历 `lst` 和 `filter`，并根据元素是否通过筛选条件将它们添加到相应的列表中。

```python
def bifurcate(lst, filter):
  return [
    [x for x, flag in zip(lst, filter) if flag],
    [x for x, flag in zip(lst, filter) if not flag]
  ]
```

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```
