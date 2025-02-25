# Die Liste vollständig entschachteln

## Problemstellung

Schreiben Sie eine Funktion `deep_flatten(lst)`, die eine Liste `lst` als Argument nimmt und eine neue Liste zurückgibt, die die vollständig entschachtelte Version von `lst` ist. Die Funktion sollte rekursiv arbeiten und die `isinstance()`-Funktion mit `collections.abc.Iterable` verwenden, um zu überprüfen, ob ein Element iterierbar ist. Wenn ein Element iterierbar ist, sollte die Funktion `deep_flatten()` rekursiv auf das Element angewendet werden. Andernfalls sollte die Funktion eine Liste zurückgeben, die nur dieses Element enthält.

## Beispiel

```python
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
deep_flatten([1, [2, [3, [4]]]]) # [1, 2, 3, 4]
deep_flatten([1, 2, 3, 4]) # [1, 2, 3, 4]
deep_flatten([]) # []
```
