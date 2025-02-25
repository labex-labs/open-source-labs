# Datumsunterschied in Tagen

## Problemstellung

Schreiben Sie eine Funktion `days_diff(start, end)`, die zwei Datumsobjekte als Eingabe nimmt und die Anzahl der Tage zwischen ihnen zurückgibt. Die Funktion sollte `start` von `end` abziehen und `datetime.timedelta.days` verwenden, um den Tagesunterschied zu erhalten.

## Beispiel

```python
from datetime import date

assert days_diff(date(2020, 10, 25), date(2020, 10, 28)) == 3
assert days_diff(date(2021, 1, 1), date(2021, 1, 1)) == 0
assert days_diff(date(2021, 1, 1), date(2021, 1, 2)) == 1
```
