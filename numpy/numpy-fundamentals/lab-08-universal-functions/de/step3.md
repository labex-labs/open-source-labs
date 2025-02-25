# Bestimmung des Ausgabetyps

Wenn nicht alle Eingabeargumente ndarrays sind, ist die Ausgabe einer ufunc nicht notwendigerweise ein ndarray. Der Ausgabetyp kann basierend auf den Eingabetypen und den Regeln der Typumwandlung bestimmt werden. Schauen wir uns ein Beispiel an.

```python
import numpy as np

# Erstellen Sie ein Array
arr = np.arange(9).reshape(3, 3)

# Führen Sie eine Multiplikation durch und geben Sie den Ausgabetyp an
result = np.multiply.reduce(arr, dtype=float)

# Drucken Sie das Ergebnis
print(result)
```

Ausgabe:

```
array([ 0., 28., 80.])
```
