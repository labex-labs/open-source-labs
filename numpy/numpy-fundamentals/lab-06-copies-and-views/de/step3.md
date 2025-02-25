# Kopien erstellen

Kopien können erstellt werden, indem sowohl der Datenpuffer als auch die Metadaten eines Arrays dupliziert werden. Um eine Kopie zu erstellen, können Sie die `copy()`-Methode des `ndarray`-Objekts verwenden.

```python
import numpy as np

# Erstellen eines Arrays
x = np.array([1, 2, 3, 4, 5])

# Erstellen einer Kopie
y = x.copy()

# Ändern der Kopie
y[0] = 10

# Ausgabe des ursprünglichen Arrays
print(x)  # Ausgabe: [1, 2, 3, 4, 5]
```

Im obigen Beispiel ist die Kopie `y` unabhängig vom ursprünglichen Array `x`.
