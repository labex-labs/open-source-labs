# Ufunc-Methoden

Ufuncs haben vier Methoden: reduce, accumulate, reduceat und outer. Diese Methoden sind nützlich für die Ausführung von Operationen auf Arrays. Schauen wir uns die reduce-Methode an.

```python
import numpy as np

# Erstellen Sie ein Array
arr = np.arange(9).reshape(3, 3)

# Reduzieren Sie das Array entlang der ersten Achse
result = np.add.reduce(arr, 1)

# Drucken Sie das Ergebnis
print(result)
```

Ausgabe:

```
array([ 3, 12, 21])
```
