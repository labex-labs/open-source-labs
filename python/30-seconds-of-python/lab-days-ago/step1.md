# Days Ago

Your task is to write a function called `days_ago(n)` that takes an integer `n` as an argument and returns the date of `n` days ago from today.

To solve this problem, you need to use the `date` class from the `datetime` module to get the current date and the `timedelta` class to subtract `n` days from the current date.

```py
from datetime import timedelta, date

def days_ago(n):
  return date.today() - timedelta(n)
```

```py
days_ago(5) # date(2020, 10, 23)
```
