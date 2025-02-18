# Datumsdifferenz

Schreiben Sie eine Funktion namens `months_diff(start, end)`, die zwei Datumsobjekte entgegennimmt und die Monatsdifferenz zwischen ihnen zurückgibt. Die Funktion sollte:

1. `start` von `end` subtrahieren und `datetime.timedelta.days` verwenden, um die Tagendifferenz zu erhalten.
2. Durch `30` teilen und `math.ceil()` verwenden, um die Differenz in Monaten zu erhalten (aufgerundet).

```python
from math import ceil

def months_diff(start, end):
  return ceil((end - start).days / 30)
```

```python
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```
