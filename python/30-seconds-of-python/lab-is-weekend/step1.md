# Date is Weekend

Write a function `is_weekend(d)` that takes a date object as input and returns `True` if the given date is a weekend, and `False` otherwise. If no argument is provided, the function should use the current date.

To solve this problem, you can follow these steps:

1. Use the `datetime.datetime.weekday()` method to get the day of the week as an integer.
2. Check if the day of the week is greater than `4`. If it is, return `True`, otherwise return `False`.

```python
from datetime import datetime

def is_weekend(d = datetime.today()):
  return d.weekday() > 4
```

```python
from datetime import date

is_weekend(date(2020, 10, 25)) # True
is_weekend(date(2020, 10, 28)) # False
```
