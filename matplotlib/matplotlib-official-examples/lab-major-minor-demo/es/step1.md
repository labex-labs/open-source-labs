# Importar las bibliotecas necesarias y crear datos

```python
import matplotlib.pyplot as plt
import numpy as np

# Crear datos
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * np.exp(-t * 0.01)
```

En primer lugar, importamos las bibliotecas necesarias, es decir, Matplotlib y NumPy. Luego creamos los datos para graficar. En este ejemplo, creamos una matriz de numpy "t" y calculamos otra matriz de numpy "s" utilizando t.
