# Liste mit Werten initialisieren

Schreiben Sie eine Funktion `initialize_list_with_values(n, val=0)`, die zwei Parameter annimmt:

- `n` (ganzzahlig), der die Länge der zu erstellenden Liste darstellt.
- `val` (ganzzahlig), der der Wert ist, der zur Befüllung der Liste verwendet werden soll. Wenn `val` nicht angegeben wird, sollte der Standardwert `0` verwendet werden.

Die Funktion sollte eine Liste der Länge `n` zurückgeben, die mit dem angegebenen Wert gefüllt ist.

```python
def initialize_list_with_values(n, val = 0):
  return [val for x in range(n)]
```

```python
initialize_list_with_values(5, 2) # [2, 2, 2, 2, 2]
```
