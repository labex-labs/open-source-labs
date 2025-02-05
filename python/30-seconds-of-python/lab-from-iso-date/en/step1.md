# Convert ISO Date

Write a function `from_iso_date(d)` that takes a string `d` representing a date in ISO-8601 format and returns a `datetime.datetime` object representing the same date and time.

```python
from datetime import datetime

def from_iso_date(d):
  return datetime.fromisoformat(d)
```

```python
from_iso_date('2020-10-28T12:30:59.000000') # 2020-10-28 12:30:59
```
