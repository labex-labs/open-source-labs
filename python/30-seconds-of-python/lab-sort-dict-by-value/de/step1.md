# Wörterbuch sortieren

Schreiben Sie eine Funktion namens `sort_dict_by_value(d, reverse=False)`, die ein Wörterbuch `d` annimmt und es nach seinen Werten sortiert. Die Funktion sollte ein neues Wörterbuch zurückgeben, das die gleichen Schlüssel wie das ursprüngliche Wörterbuch hat, aber die Werte in aufsteigender Reihenfolge sortiert sind. Wenn der Parameter `reverse` auf `True` gesetzt ist, sollte die Funktion das Wörterbuch in absteigender Reihenfolge sortieren.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `dict.items()`, um eine Liste von Tupelpaaren aus `d` zu erhalten.
2. Sortieren Sie die Liste mit einer Lambda-Funktion und `sorted()`.
3. Verwenden Sie `dict()`, um die sortierte Liste wieder in ein Wörterbuch umzuwandeln.
4. Verwenden Sie den Parameter `reverse` in `sorted()`, um das Wörterbuch in umgekehrter Reihenfolge zu sortieren, basierend auf dem zweiten Argument.

**⚠️ ACHTUNG:** Die Werte des Wörterbuchs müssen vom gleichen Typ sein.

```python
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_value(d) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
sort_dict_by_value(d, True)
# {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
```
