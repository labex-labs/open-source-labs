# N kleinste Elemente

## Problem

Schreiben Sie eine Funktion namens `min_n(lst, n = 1)`, die eine Liste `lst` und einen optionalen Integer `n` (Standardwert `1`) annimmt. Die Funktion sollte eine neue Liste zurückgeben, die die `n` kleinsten Elemente aus der ursprünglichen Liste `lst` enthält. Wenn `n` nicht angegeben wird, sollte die Funktion eine Liste zurückgeben, die das kleinste Element aus `lst` enthält.

Wenn `n` größer als oder gleich der Länge von `lst` ist, sollte die Funktion die ursprüngliche Liste in aufsteigender Reihenfolge zurückgeben.

Ihre Funktion sollte dies durch die folgenden Schritte erreichen:

1. Verwenden Sie die integrierte `sorted()`-Funktion, um die Liste in aufsteigender Reihenfolge zu sortieren.
2. Verwenden Sie die Slicenotation, um die angegebene Anzahl von Elementen zu erhalten.
3. Geben Sie die resultierende Liste zurück.

## Beispiel

```python
min_n([1, 2, 3]) # [1]
min_n([1, 2, 3], 2) # [1, 2]
```
