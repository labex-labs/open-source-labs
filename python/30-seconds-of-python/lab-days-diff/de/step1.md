# Datumsunterschied in Tagen

Schreiben Sie eine Funktion `days_diff(start, end)`, die zwei Datumsobjekte als Eingabe nimmt und die Anzahl der Tage zwischen ihnen zurückgibt. Die Funktion sollte `start` von `end` subtrahieren und `datetime.timedelta.days` verwenden, um den Tagesunterschied zu erhalten.

```python
def days_diff(start, end):
  return (end - start).days
```

```python
from datetime import date

days_diff(date(2020, 10, 25), date(2020, 10, 28)) # 3
```
