---
title: Days from now
---

Calculates the date of `n` days from today.

- Use `datetime.date.today()` to get the current day.
- Use `datetime.timedelta` to add `n` days from today's date.

```py
from datetime import timedelta, date

def days_from_now(n):
  return date.today() + timedelta(n)
```

```py
days_from_now(5) # date(2020, 11, 02)
```
