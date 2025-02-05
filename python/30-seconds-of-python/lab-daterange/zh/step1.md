# 日期范围

编写一个名为 `daterange(start, end)` 的 Python 函数，该函数接受两个 `datetime.date` 对象作为参数，并返回它们之间的所有日期的列表。该列表应包括开始日期但不包括结束日期。

要解决此问题，你可以按照以下步骤操作：

1. 使用 `datetime.timedelta.days` 获取 `start` 和 `end` 之间的天数。
2. 使用 `int()` 将结果转换为整数，并使用 `range()` 遍历每一天。
3. 使用列表推导式和 `datetime.timedelta` 创建一个 `datetime.date` 对象的列表。

```python
from datetime import timedelta, date

def daterange(start, end):
  return [start + timedelta(n) for n in range(int((end - start).days))]
```

```python
from datetime import date

daterange(date(2020, 10, 1), date(2020, 10, 5))
# [date(2020, 10, 1), date(2020, 10, 2), date(2020, 10, 3), date(2020, 10, 4)]
```
