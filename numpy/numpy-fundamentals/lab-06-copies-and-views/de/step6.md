# Bestimmen, ob ein Array eine Ansicht oder eine Kopie ist

Sie können das `base`-Attribut des `ndarray`-Objekts verwenden, um zu bestimmen, ob ein Array eine Ansicht oder eine Kopie ist. Das `base`-Attribut gibt das ursprüngliche Array für eine Ansicht zurück und `None` für eine Kopie. Beispielsweise:

```python
import numpy as np

# Erstellen eines Arrays
x = np.arange(9)

# Erstellen einer Ansicht
y = x.reshape(3, 3)

# Erstellen einer Kopie
z = y[[2, 1]]

# Überprüfen, ob y eine Ansicht ist
print(y.base)  # Ausgabe: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Überprüfen, ob z eine Kopie ist
print(z.base is None)  # Ausgabe: True
```

Im obigen Beispiel ist `y` eine Ansicht und `z` eine Kopie.
