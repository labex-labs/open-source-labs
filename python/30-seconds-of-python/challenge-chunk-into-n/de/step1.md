# Liste in N Blöcke teilen

## Problemstellung

Schreiben Sie eine Python-Funktion namens `chunk_into_n(lst, n)`, die eine Liste `lst` und eine ganze Zahl `n` als Eingabe nimmt und eine Liste von `n` kleineren Listen zurückgibt, wobei jede Liste eine gleiche Anzahl von Elementen aus der ursprünglichen Liste enthält. Wenn die ursprüngliche Liste nicht gleichmäßig in `n` kleinere Listen aufgeteilt werden kann, soll der letzte Block die verbleibenden Elemente enthalten.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Berechnen Sie die Größe jedes Blocks, indem Sie die Länge der ursprünglichen Liste durch `n` dividieren und auf die nächste ganze Zahl aufrunden, indem Sie die `math.ceil()`-Funktion verwenden.
2. Erstellen Sie eine neue Liste der Größe `n` mit den Funktionen `list()` und `range()`.
3. Verwenden Sie die `map()`-Funktion, um jedes Element der neuen Liste einem Block der ursprünglichen Liste der Länge `size` zuzuordnen.
4. Geben Sie die Liste der kleineren Listen zurück.

Ihre Funktion sollte folgende Signatur haben:

```python
def chunk_into_n(lst: list, n: int) -> list:
```

## Beispiel

```python
assert chunk_into_n([1, 2, 3, 4, 5, 6, 7], 4) == [[1, 2], [3, 4], [5, 6], [7]]
assert chunk_into_n([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]
assert chunk_into_n([1, 2, 3, 4, 5, 6, 7], 2) == [[1, 2, 3, 4], [5, 6, 7]]
assert chunk_into_n([1, 2, 3, 4, 5, 6, 7], 1) == [[1, 2, 3, 4, 5, 6, 7]]
```
