# Ziffern einer Zahl extrahieren

Schreiben Sie eine Funktion `digitize(n)`, die eine nicht-negative Ganzzahl `n` als Eingabe nimmt und eine Liste ihrer Ziffern zurückgibt. Die Funktion sollte dies erreichen, indem sie die folgenden Schritte ausführt:

1. Konvertieren Sie die Eingabezahl `n` in eine Zeichenkette (string).
2. Verwenden Sie die `map()`-Funktion in Kombination mit der `int`-Funktion, um jedes Zeichen in der Zeichenkette in eine Ganzzahl umzuwandeln.
3. Geben Sie die resultierende Liste von Ganzzahlen zurück.

Beispielsweise sollte die Funktion, wenn die Eingabezahl `123` ist, die Liste `[1, 2, 3]` zurückgeben.

```python
def digitize(n):
  return list(map(int, str(n)))
```

```python
digitize(123) # [1, 2, 3]
```
