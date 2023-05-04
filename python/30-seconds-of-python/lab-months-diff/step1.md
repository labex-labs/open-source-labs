# Date Difference Challenge

Write a function called `months_diff(start, end)` that takes in two date objects and returns the month difference between them. The function should:

1. Subtract `start` from `end` and use `datetime.timedelta.days` to get the day difference.
2. Divide by `30` and use `math.ceil()` to get the difference in months (rounded up).

```py
from math import ceil

def months_diff(start, end):
  return ceil((end - start).days / 30)
```

```py
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```
