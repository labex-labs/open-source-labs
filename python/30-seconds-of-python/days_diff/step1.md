# Date Difference in Days

## Problem
Write a function `days_diff(start, end)` that takes two date objects as input and returns the number of days between them. The function should subtract `start` from `end` and use `datetime.timedelta.days` to get the day difference.

## Example
```py
from datetime import date

assert days_diff(date(2020, 10, 25), date(2020, 10, 28)) == 3
assert days_diff(date(2021, 1, 1), date(2021, 1, 1)) == 0
assert days_diff(date(2021, 1, 1), date(2021, 1, 2)) == 1
```

