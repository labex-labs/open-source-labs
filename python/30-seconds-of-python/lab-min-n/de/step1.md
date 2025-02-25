# N kleinste Elemente

Schreibe eine Funktion namens `min_n(lst, n = 1)`, die eine Liste `lst` und einen optionalen Integer `n` (Standardwert `1`) annimmt. Die Funktion sollte eine neue Liste zurückgeben, die die `n` kleinsten Elemente aus der ursprünglichen Liste `lst` enthält. Wenn `n` nicht angegeben wird, sollte die Funktion eine Liste zurückgeben, die das kleinste Element aus `lst` enthält.

Wenn `n` größer als oder gleich der Länge von `lst` ist, sollte die Funktion die ursprüngliche Liste in aufsteigender Reihenfolge zurückgeben.

Deine Funktion sollte dies durch die folgenden Schritte erreichen:

1. Verwende die eingebautte `sorted()`-Funktion, um die Liste in aufsteigender Reihenfolge zu sortieren.
2. Verwende Slicenotation, um die angegebene Anzahl von Elementen zu erhalten.
3. Gebe die resultierende Liste zurück.

```python
def min_n(lst, n = 1):
  return sorted(lst, reverse = False)[:n]
```

```python
min_n([1, 2, 3]) # [1]
min_n([1, 2, 3], 2) # [1, 2]
```
