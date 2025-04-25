# 中位数

编写一个名为 `find_median` 的 Python 函数，该函数接受一个数字列表作为参数，并返回该列表的中位数。你的函数应执行以下步骤：

1. 使用 `list.sort()` 对列表中的数字进行排序。
2. 找到中位数，如果列表长度为奇数，则中位数是列表的中间元素；如果列表长度为偶数，则中位数是两个中间元素的平均值。
3. 返回中位数。

你的函数不应使用任何直接解决该问题的 Python 内置库或函数。

```python
def median(list):
  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return float(list[int(list_length / 2)])
```

```python
median([1, 2, 3]) # 2.0
median([1, 2, 3, 4]) # 2.5
```
