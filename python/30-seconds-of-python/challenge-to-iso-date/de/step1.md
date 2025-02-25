# Datum in ISO-Format

## Problemstellung

Schreiben Sie eine Funktion `to_iso_date(d)`, die ein `datetime.datetime`-Objekt als Argument nimmt und einen String zurückgibt, der das Datum im ISO-8601-Format repräsentiert. Die Funktion sollte die `datetime.datetime.isoformat()`-Methode verwenden, um das Datum in seine ISO-8601-Darstellung zu konvertieren.

## Beispiel

```python
from datetime import datetime

to_iso_date(datetime(2020, 10, 25)) # "2020-10-25T00:00:00"
```
