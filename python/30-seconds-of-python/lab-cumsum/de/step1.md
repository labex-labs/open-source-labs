# Liste von partiellen Summen

Schreiben Sie eine Funktion `partial_sum(lst)`, die eine Liste von Zahlen als Argument nimmt und eine Liste von partiellen Summen zurückgibt. Ihre Funktion sollte die folgenden Schritte ausführen:

1. Verwenden Sie `itertools.accumulate()`, um die kumulative Summe für jedes Element in der Liste zu erstellen.
2. Verwenden Sie `list()`, um das Ergebnis in eine Liste zu konvertieren.
3. Geben Sie die Liste der partiellen Summen zurück.

```python
from itertools import accumulate

def cumsum(lst):
  return list(accumulate(lst))
```

```python
cumsum(range(0, 15, 3)) # [0, 3, 9, 18, 30]
```
