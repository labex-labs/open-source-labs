# Grundlegende arithmetische Operationen

Die grundlegenden ufuncs operieren auf Skalaren, und das einfachste Beispiel ist der Additionoperator. Schauen wir uns an, wie wir den Additionoperator verwenden können, um zwei Arrays elementweise zu addieren.

```python
import numpy as np

# Erstellen Sie zwei Arrays
arr1 = np.array([0, 2, 3, 4])
arr2 = np.array([1, 1, -1, 2])

# Addieren Sie die Arrays elementweise
result = arr1 + arr2

# Drucken Sie das Ergebnis
print(result)
```

Ausgabe:

```
array([1, 3, 2, 6])
```
