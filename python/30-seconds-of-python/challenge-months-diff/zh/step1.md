# 日期差挑战

## 问题

编写一个名为 `months_diff(start, end)` 的函数，该函数接受两个日期对象，并返回它们之间的月份差。该函数应：

1. 用 `end` 减去 `start`，并使用 `datetime.timedelta.days` 获取天数差。
2. 除以 `30`，并使用 `math.ceil()` 获取月份差（向上取整）。

## 示例

```python
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```
