# Weitere Operationen

Es gibt weitere Operationen in NumPy, die Ansichten oder Kopien erzeugen können.

- Die `reshape()`-Funktion erzeugt, soweit möglich, eine Ansicht, andernfalls eine Kopie. Beispielsweise:

```python
import numpy as np

# Erstellen eines Arrays
x = np.ones((2, 3))

# Transponieren des Arrays
y = x.T

# Versuch, das Array umzuformen
try:
    y.shape = 6
except AttributeError:
    print("Incompatible shape for in-place modification. Use `.reshape()` to make a copy with the desired shape.")
```

Im obigen Beispiel wird das Array `y` nach der Transposition nicht mehr zusammenhängend, sodass seine Umformung eine Kopie erfordert.

- Die `ravel()`-Funktion gibt, soweit möglich, eine zusammenhängende abgeflachte Ansicht des Arrays zurück. Dagegen gibt die `flatten()`-Methode immer eine abgeflachte Kopie des Arrays zurück. Beispielsweise:

```python
import numpy as np

# Erstellen eines Arrays
x = np.arange(9).reshape(3, 3)

# Erstellen einer abgeflachten Ansicht
y = x.ravel()

# Erstellen einer abgeflachten Kopie
z = x.flatten()

# Ausgabe des ursprünglichen Arrays
print(x)  # Ausgabe: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

Im obigen Beispiel ist `y` eine Ansicht, während `z` eine Kopie ist.
