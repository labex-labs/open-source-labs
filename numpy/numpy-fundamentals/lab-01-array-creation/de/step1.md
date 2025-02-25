# Konvertieren von Python-Sequenzen in NumPy-Arrays

Um NumPy-Arrays zu erstellen, können Sie Python-Sequenzen wie Listen und Tupel umwandeln. Hier ist, wie Sie es tun können:

```python
import numpy as np

# Erstellen eines 1D-Arrays aus einer Liste
a1D = np.array([1, 2, 3, 4])

# Erstellen eines 2D-Arrays aus einer Liste von Listen
a2D = np.array([[1, 2], [3, 4]])

# Erstellen eines 3D-Arrays aus geschachtelten Listen
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

Wenn Sie Arrays erstellen, können Sie auch den Datentyp mit dem Parameter `dtype` angeben. Seien Sie bei der Datentyp-Zuweisung vorsichtig, um Überläufe oder unerwartete Ergebnisse zu vermeiden.
