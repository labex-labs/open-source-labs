# Verwenden von eingebauten NumPy-Array-Erstellungsfunktionen

NumPy bietet eingebautes Funktionen zur Erstellung von Arrays. Hier sind einige Beispiele:

```python
import numpy as np

# Erstellen eines 1D-Arrays mit regelmäßig zunehmenden Werten
arr1D = np.arange(10)

# Erstellen eines 1D-Arrays mit einem bestimmten Datentyp
arr1D_float = np.arange(2, 10, dtype=float)

# Erstellen eines 1D-Arrays mit einer bestimmten Anzahl von Elementen
arr1D_linspace = np.linspace(1., 4., 6)

# Erstellen einer 2D-Einheitsmatrix
identity_matrix = np.eye(3)

# Erstellen einer 2D-Matrix mit gegebenen Werten entlang der Diagonalen
diag_matrix = np.diag([1, 2, 3])

# Erstellen einer Vandermonde-Matrix
vander_matrix = np.vander([1, 2, 3, 4], 2)

# Erstellen eines Arrays, das mit Nullen gefüllt ist
zeros_array = np.zeros((2, 3))

# Erstellen eines Arrays, das mit Einsen gefüllt ist
ones_array = np.ones((2, 3))

# Erstellen eines Arrays, das mit zufälligen Werten gefüllt ist
random_array = np.random.default_rng(42).random((2, 3))
```
