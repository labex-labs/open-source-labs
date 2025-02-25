# Ungleichheitsausreißer finden

## Problem

Schreiben Sie eine Funktion `find_parity_outliers(nums)`, die eine Liste von ganzen Zahlen `nums` als Argument nimmt und eine Liste aller Ungleichheitsausreißer in `nums` zurückgibt.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `collections.Counter` mit einer Listenkomprehension, um die Anzahl der geraden und ungeraden Werte in der Liste zu zählen.
2. Verwenden Sie `collections.Counter.most_common()`, um die häufigste Parität zu erhalten.
3. Verwenden Sie eine Listenkomprehension, um alle Elemente zu finden, die nicht der häufigsten Parität entsprechen.

## Beispiel

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```

Im obigen Beispiel ist die Mehrheit der Elemente in der Liste gerade, so dass die Ungleichheitsausreißer die ungeraden Elemente 1 und 3 sind.
