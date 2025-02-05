# 合并列表

编写一个名为 `merge(*args, fill_value=None)` 的函数，它接受两个或更多列表作为参数，并返回一个列表的列表。该函数应根据输入列表中元素的位置将它们组合起来。如果某个列表比最长的列表短，函数应用 `fill_value` 填充剩余的元素。如果未提供 `fill_value`，则应默认为 `None`。

你的任务是实现 `merge()` 函数。

```python
def merge(*args, fill_value = None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
```

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```
