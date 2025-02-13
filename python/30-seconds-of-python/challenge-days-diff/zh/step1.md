# 日期相差天数

## 问题

编写一个函数 `days_diff(start, end)`，该函数接受两个日期对象作为输入，并返回它们之间相差的天数。该函数应从 `end` 中减去 `start`，并使用 `datetime.timedelta.days` 来获取天数差。

## 示例

```python
from datetime import date

assert days_diff(date(2020, 10, 25), date(2020, 10, 28)) == 3
assert days_diff(date(2021, 1, 1), date(2021, 1, 1)) == 0
assert days_diff(date(2021, 1, 1), date(2021, 1, 2)) == 1
```
