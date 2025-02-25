# ISO-Datum umwandeln

Schreiben Sie eine Funktion `from_iso_date(d)`, die einen String `d` annimmt, der ein Datum im ISO-8601-Format darstellt, und gibt ein `datetime.datetime`-Objekt zurück, das das gleiche Datum und die gleiche Uhrzeit repräsentiert.

```python
from datetime import datetime

def from_iso_date(d):
  return datetime.fromisoformat(d)
```

```python
from_iso_date('2020-10-28T12:30:59.000000') # 2020-10-28 12:30:59
```
