# Add Days to Date

Write a function `add_days(n, d)` that takes in two arguments:

- `n`: an integer representing the number of days to add (if positive) or subtract (if negative) from the given date.
- `d`: an optional argument representing the date to which the days should be added or subtracted. If not provided, the current date should be used.

The function should return a `datetime` object representing the new date after adding or subtracting the specified number of days.

```py
from datetime import datetime, timedelta

def add_days(n, d = datetime.today()):
  return d + timedelta(n)
```

```py
from datetime import date

add_days(5, date(2020, 10, 25)) # date(2020, 10, 30)
add_days(-5, date(2020, 10, 25)) # date(2020, 10, 20)
```
