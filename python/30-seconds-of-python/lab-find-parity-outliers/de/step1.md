# Ungleichheitsausreißer finden

Schreiben Sie eine Funktion `find_parity_outliers(nums)`, die eine Liste von ganzen Zahlen `nums` als Argument nimmt und eine Liste aller Ungleichheitsausreißer in `nums` zurückgibt.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `collections.Counter` mit einer Listenkomprehension, um die Anzahl der geraden und ungeraden Werte in der Liste zu zählen.
2. Verwenden Sie `collections.Counter.most_common()`, um die häufigste Parität zu erhalten.
3. Verwenden Sie eine Listenkomprehension, um alle Elemente zu finden, die nicht der häufigsten Parität entsprechen.

```python
from collections import Counter

def find_parity_outliers(nums):
  return [
    x for x in nums
    if x % 2!= Counter([n % 2 for n in nums]).most_common()[0][0]
  ]
```

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```
