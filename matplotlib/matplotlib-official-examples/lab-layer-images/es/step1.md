# Importar las bibliotecas necesarias y definir una función

Importa las bibliotecas necesarias y define una función para crear la primera imagen.

```python
import matplotlib.pyplot as plt
import numpy as np

def func3(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))
```
