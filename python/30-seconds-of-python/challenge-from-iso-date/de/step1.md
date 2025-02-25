# ISO-Datum umwandeln

## Problemstellung

Schreiben Sie eine Funktion `from_iso_date(d)`, die einen String `d` annimmt, der ein Datum im ISO-8601-Format darstellt, und gibt ein `datetime.datetime`-Objekt zurück, das dasselbe Datum und die selbe Uhrzeit repräsentiert.

## Beispiel

```python
from_iso_date('2020-10-28T12:30:59.000000') # gibt datetime.datetime(2020, 10, 28, 12, 30, 59) zurück
```
