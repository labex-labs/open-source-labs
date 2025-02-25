# Ansichten erstellen

Ansichten können erstellt werden, indem bestimmte Metadaten eines Arrays geändert werden. Dadurch wird eine neue Art der Betrachtung der Daten erzeugt, ohne dass diese kopiert werden. Um eine Ansicht zu erstellen, können Sie die `view()`-Methode des `ndarray`-Objekts verwenden.

```python
import numpy as np

# Erstellen eines Arrays
x = np.array([1, 2, 3, 4, 5])

# Erstellen einer Ansicht
y = x.view()

# Ändern der Ansicht
y[0] = 10

# Ausgabe des ursprünglichen Arrays
print(x)  # Ausgabe: [10, 2, 3, 4, 5]
```

Im obigen Beispiel ermöglicht die Ansicht `y` uns, das ursprüngliche Array `x` zu ändern.
