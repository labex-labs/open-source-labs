# Check if a Date is a Weekday

Write a Python function called `is_weekday()` that takes a date as input and returns `True` if it is a weekday, and `False` if it is a weekend. If no date is provided, the function should use the current date.

To solve this problem, you can follow these steps:

1. Import the `datetime` module.
2. Define a function called `is_weekday()` that takes a date as input. If no date is provided, use the current date.
3. Use the `weekday()` method of the `datetime` module to get the day of the week as an integer. The `weekday()` method returns an integer between 0 (Monday) and 6 (Sunday).
4. Check if the day of the week is less than or equal to 4. If it is, return `True`, otherwise return `False`.

```python
from datetime import datetime

def is_weekday(d = datetime.today()):
  return d.weekday() <= 4
```

```python
from datetime import date

is_weekday(date(2020, 10, 25)) # False
is_weekday(date(2020, 10, 28)) # True
```
