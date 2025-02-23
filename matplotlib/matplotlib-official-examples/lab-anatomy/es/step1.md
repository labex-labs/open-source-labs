# Importar bibliotecas y configurar datos

Primero, necesitamos importar las bibliotecas necesarias y configurar algunos datos para graficar. En este ejemplo, graficaremos tres ondas senoidales con un poco de ruido aleatorio agregado.

```python
import matplotlib.pyplot as plt
import numpy as np

# Configurar datos
np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))
```
