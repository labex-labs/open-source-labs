# For-Schleifen und Tupel

Sie können mit mehreren Iterationsvariablen iterieren.

```python
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    # Schleifen mit x = 1, y = 4
    #            x = 10, y = 40
    #            x = 23, y = 14
    #           ...
```

Wenn Sie mehrere Variablen verwenden, wird jedes Tupel in eine Reihe von Iterationsvariablen _aufgelöst_. Die Anzahl der Variablen muss der Anzahl der Elemente in jedem Tupel entsprechen.
