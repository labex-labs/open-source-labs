# Days from now

Write a function `days_from_now(n)` that takes an integer `n` as input and returns the date of `n` days from today.

To solve this problem, you can follow these steps:

1. Import the `datetime` module.
2. Use the `date.today()` method to get the current date.
3. Use the `timedelta` method to add `n` days to the current date.
4. Return the new date.

```py
from datetime import timedelta, date

def days_from_now(n):
  return date.today() + timedelta(n)
```

```py
days_from_now(5) # date(2020, 11, 02)
```
