# Date to ISO format

Write a function `to_iso_date(d)` that takes a `datetime.datetime` object as its argument and returns a string representing the date in ISO-8601 format. The function should use the `datetime.datetime.isoformat()` method to convert the date to its ISO-8601 representation.

```python
from datetime import datetime

def to_iso_date(d):
  return d.isoformat()
```

```python
from datetime import datetime

to_iso_date(datetime(2020, 10, 25)) # 2020-10-25T00:00:00
```
