# Importez les bibliothèques nécessaires et définissez une fonction

Importez les bibliothèques nécessaires et définissez une fonction pour créer la première image.

```python
import matplotlib.pyplot as plt
import numpy as np

def func3(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))
```
