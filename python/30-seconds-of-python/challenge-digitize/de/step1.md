# Zahl in einzelne Ziffern zerlegen

## Problemstellung

Schreiben Sie eine Funktion `digitize(n)`, die eine nicht-negative ganze Zahl `n` als Eingabe nimmt und eine Liste ihrer Ziffern zurückgibt. Die Funktion soll dies durch die folgenden Schritte erreichen:

1. Konvertieren Sie die Eingabzahl `n` in einen String.
2. Verwenden Sie die `map()`-Funktion in Kombination mit der `int`-Funktion, um jedes Zeichen im String in eine Ganzzahl umzuwandeln.
3. Geben Sie die resultierende Liste von Ganzzahlen zurück.

Beispielsweise sollte die Funktion für die Eingabzahl `123` die Liste `[1, 2, 3]` zurückgeben.

## Beispiel

```python
assert digitize(123) == [1, 2, 3]
assert digitize(4567) == [4, 5, 6, 7]
assert digitize(0) == [0]
```
