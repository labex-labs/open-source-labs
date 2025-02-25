# Datumsdifferenz-Aufgabe

## Problemstellung

Schreiben Sie eine Funktion namens `months_diff(start, end)`, die zwei Datumsobjekte als Parameter annimmt und die Monatsdifferenz zwischen ihnen zurückgibt. Die Funktion soll Folgendes tun:

1. Subtrahieren Sie `start` von `end` und verwenden Sie `datetime.timedelta.days`, um die Tagesdifferenz zu erhalten.
2. Teilen Sie die Tagesdifferenz durch `30` und verwenden Sie `math.ceil()`, um die Differenz in Monaten zu erhalten (aufgerundet).

## Beispiel

```python
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```
