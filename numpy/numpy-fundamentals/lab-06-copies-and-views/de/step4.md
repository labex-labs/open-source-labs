# Indexierungsoperationen

Indexierungsoperationen in NumPy können entweder Ansichten oder Kopien erzeugen, je nachdem, um welche Art der Indexierung es sich handelt.

- Die einfache Indexierung erzeugt immer Ansichten. Beispielsweise:

```python
import numpy as np

# Erstellen eines Arrays
x = np.arange(10)

# Erstellen einer Ansicht
y = x[1:3]

# Ändern der Ansicht
y[0] = 10

# Ausgabe des ursprünglichen Arrays
print(x)  # Ausgabe: [0, 10, 2, 3, 4, 5, 6, 7, 8, 9]
```

Im obigen Beispiel spiegelt die Ansicht `y` die Änderungen wider, die am ursprünglichen Array `x` vorgenommen wurden.

- Die fortgeschrittene Indexierung erzeugt immer Kopien. Beispielsweise:

```python
import numpy as np

# Erstellen eines Arrays
x = np.arange(9).reshape(3, 3)

# Erstellen einer Kopie
y = x[[1, 2]]

# Ändern des ursprünglichen Arrays
x[[1, 2]] = [[10, 11, 12], [13, 14, 15]]

# Ausgabe der Kopie
print(y)  # Ausgabe: [[3, 4, 5], [6, 7, 8]]
```

Im obigen Beispiel bleibt die Kopie `y` unverändert, nachdem das ursprüngliche Array `x` geändert wurde.
