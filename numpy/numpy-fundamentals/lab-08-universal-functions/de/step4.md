# Broadcasting

Broadcasting ist ein leistungsstarkes Feature von ufuncs, das es ermöglicht, Operationen auf Arrays mit unterschiedlichen Formen durchzuführen. Die Broadcasting-Regeln bestimmen, wie Arrays mit unterschiedlichen Formen während der Operationen behandelt werden. Schauen wir uns ein Beispiel an.

```python
import numpy as np

# Erstellen Sie zwei Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1], [2], [3]])

# Multiplizieren Sie die Arrays
result = arr1 * arr2

# Drucken Sie das Ergebnis
print(result)
```

Ausgabe:

```
array([[1, 2, 3],
       [2, 4, 6],
       [3, 6, 9]])
```
