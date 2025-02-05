# 日期差值

编写一个名为 `months_diff(start, end)` 的函数，该函数接受两个日期对象，并返回它们之间的月份差值。该函数应：

1. 用 `end` 减去 `start`，并使用 `datetime.timedelta.days` 获取日差值。
2. 除以 `30`，并使用 `math.ceil()` 获取月份差值（向上取整）。

```python
from math import ceil

def months_diff(start, end):
  return ceil((end - start).days / 30)
```

```python
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```
