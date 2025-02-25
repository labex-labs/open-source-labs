# Initialisiere eine zweidimensionale Liste

Schreibe eine Funktion `initialize_2d_list(w, h, val=None)`, die eine zweidimensionale Liste der angegebenen Breite, Höhe und Wert initialisiert. Die Funktion sollte eine Liste von `h` Zeilen zurückgeben, wobei jede Zeile eine Liste mit der Länge `w` ist, die mit `val` initialisiert ist. Wenn `val` nicht angegeben ist, sollte der Standardwert `None` sein.

```python
def initialize_2d_list(w, h, val = None):
  return [[val for x in range(w)] for y in range(h)]
```

```python
initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
```
