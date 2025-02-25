# Entferne Listelemente von Ende

Schreiben Sie eine Funktion `take_right(lst, n=1)`, die eine Liste `lst` und einen optionalen Integer `n` als Argumente nimmt und eine neue Liste zurückgibt, aus der `n` Elemente von Ende entfernt wurden. Wenn `n` nicht angegeben wird, sollte die Funktion nur das letzte Element aus der Liste entfernen.

Um dieses Problem zu lösen, können Sie die Slicenotation verwenden, um einen Schnitt der Liste zu erstellen, bei dem `n` Elemente von Ende genommen werden.

```python
def take_right(itr, n = 1):
  return itr[-n:]
```

```python
take_right([1, 2, 3], 2) # [2, 3]
take_right([1, 2, 3]) # [3]
```
