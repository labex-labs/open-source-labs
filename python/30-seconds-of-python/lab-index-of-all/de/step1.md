# Alle Indizes eines Werts

Schreiben Sie eine Python-Funktion namens `index_of_all(lst, value)`, die eine Liste `lst` und einen Wert `value` als Argumente nimmt und eine Liste von Indizes aller Vorkommen von `value` in `lst` zurückgibt.

Um dieses Problem zu lösen, können Sie `enumerate()` und eine Listenkomprehension verwenden, um jedes Element auf Gleichheit mit `value` zu überprüfen und `i` zum Ergebnis hinzuzufügen.

```python
def index_of_all(lst, value):
  return [i for i, x in enumerate(lst) if x == value]
```

```python
index_of_all([1, 2, 1, 4, 5, 1], 1) # [0, 2, 5]
index_of_all([1, 2, 3, 4], 6) # []
```
