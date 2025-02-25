# Replizieren, Verbinden oder Verändern von vorhandenen Arrays

Sobald Sie Arrays erstellt haben, können Sie sie replizieren, verbinden oder verändern, um neue Arrays zu erstellen. Wenn Sie ein Array oder seine Elemente an eine neue Variable zuweisen, verwenden Sie die `np.copy`-Funktion, um ein neues Array zu erstellen, anstatt eine Sicht in das ursprüngliche Array zu erzeugen. Hier ist ein Beispiel:

```python
import numpy as np

# Erstellen eines Arrays
a = np.array([1, 2, 3, 4])

# Erstellen einer Sicht der ersten beiden Elemente des Arrays
b = a[:2]

# Ändern der Sicht
b += 1

# Drucken des ursprünglichen Arrays und der geänderten Sicht
print('a =', a, '; b =', b)
```

Um Arrays zu verbinden, können Sie Funktionen wie `np.vstack`, `np.hstack` und `np.block` verwenden. Hier ist ein Beispiel zum Verbinden von vier 2x2-Arrays zu einem 4x4-Array mit `np.block`:

```python
import numpy as np

A = np.ones((2, 2))
B = np.eye(2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))

result = np.block([[A, B], [C, D]])
```
