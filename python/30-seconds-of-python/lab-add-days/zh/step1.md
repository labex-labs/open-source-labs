# 给日期增加天数

编写一个函数 `add_days(n, d)`，它接受两个参数：

- `n`：一个整数，表示要从给定日期增加（如果为正数）或减去（如果为负数）的天数。
- `d`：一个可选参数，表示要增加或减去天数的日期。如果未提供，则应使用当前日期。

该函数应返回一个 `datetime` 对象，表示在增加或减去指定天数后的新日期。

```python
from datetime import datetime, timedelta

def add_days(n, d = datetime.today()):
  return d + timedelta(n)
```

```python
from datetime import date

add_days(5, date(2020, 10, 25)) # date(2020, 10, 30)
add_days(-5, date(2020, 10, 25)) # date(2020, 10, 20)
```
