# 日期差（以天为单位）

编写一个函数 `days_diff(start, end)`，该函数接受两个日期对象作为输入，并返回它们之间的天数。该函数应从 `end` 中减去 `start`，并使用 `datetime.timedelta.days` 来获取天数差。

```python
def days_diff(start, end):
  return (end - start).days
```

```python
from datetime import date

days_diff(date(2020, 10, 25), date(2020, 10, 28)) # 3
```
