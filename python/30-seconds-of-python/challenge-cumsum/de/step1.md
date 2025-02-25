# Liste von partiellen Summen

## Problemstellung

Schreiben Sie eine Funktion `partial_sum(lst)`, die eine Liste von Zahlen als Argument nimmt und eine Liste von partiellen Summen zurückgibt. Ihre Funktion sollte die folgenden Schritte ausführen:

1. Verwenden Sie `itertools.accumulate()`, um die kumulative Summe für jedes Element in der Liste zu erstellen.
2. Verwenden Sie `list()`, um das Ergebnis in eine Liste zu konvertieren.
3. Geben Sie die Liste der partiellen Summen zurück.

## Beispiel

```python
partial_sum([1, 2, 3, 4, 5]) # [1, 3, 6, 10, 15]
partial_sum([2, 4, 6, 8, 10]) # [2, 6, 12, 20, 30]
partial_sum([5, 10, 15, 20, 25]) # [5, 15, 30, 50, 75]
```
