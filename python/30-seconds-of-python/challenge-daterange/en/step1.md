# Date Range Challenge

## Problem

Write a Python function called `daterange(start, end)` that takes two `datetime.date` objects as arguments and returns a list of all the dates between them. The list should include the start date but not the end date.

To solve this problem, you can follow these steps:

1. Use `datetime.timedelta.days` to get the number of days between `start` and `end`.
2. Use `int()` to convert the result to an integer and `range()` to iterate over each day.
3. Use a list comprehension and `datetime.timedelta` to create a list of `datetime.date` objects.

## Example

```python
from datetime import date

daterange(date(2020, 10, 1), date(2020, 10, 5))
# [date(2020, 10, 1), date(2020, 10, 2), date(2020, 10, 3), date(2020, 10, 4)]
```
