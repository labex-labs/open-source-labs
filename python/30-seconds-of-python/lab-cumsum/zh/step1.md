# 部分和列表

编写一个函数 `partial_sum(lst)`，它接受一个数字列表作为参数，并返回一个部分和的列表。你的函数应执行以下步骤：

1. 使用 `itertools.accumulate()` 为列表中的每个元素创建累积和。
2. 使用 `list()` 将结果转换为列表。
3. 返回部分和的列表。

```python
from itertools import accumulate

def cumsum(lst):
  return list(accumulate(lst))
```

```python
cumsum(range(0, 15, 3)) # [0, 3, 9, 18, 30]
```
