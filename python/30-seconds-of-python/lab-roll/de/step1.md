# Listelemente rotieren

Schreibe eine Funktion `roll(lst, offset)`, die eine Liste `lst` und eine Ganzzahl `offset` als Parameter nimmt. Die Funktion sollte die angegebene Anzahl von Elementen an den Anfang der Liste verschieben. Wenn `offset` positiv ist, sollten die Elemente von Ende der Liste zum Anfang verschoben werden. Wenn `offset` negativ ist, sollten die Elemente von Anfang der Liste zum Ende verschoben werden.

Gebe die modifizierte Liste zurück.

```python
def roll(lst, offset):
  return lst[-offset:] + lst[:-offset]
```

```python
roll([1, 2, 3, 4, 5], 2) # [4, 5, 1, 2, 3]
roll([1, 2, 3, 4, 5], -2) # [3, 4, 5, 1, 2]
```
