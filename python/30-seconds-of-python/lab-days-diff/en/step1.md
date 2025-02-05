# Date Difference in Days

Write a function `days_diff(start, end)` that takes two date objects as input and returns the number of days between them. The function should subtract `start` from `end` and use `datetime.timedelta.days` to get the day difference.

```python
def days_diff(start, end):
  return (end - start).days
```

```python
from datetime import date

days_diff(date(2020, 10, 25), date(2020, 10, 28)) # 3
```
