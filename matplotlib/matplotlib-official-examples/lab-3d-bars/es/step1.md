# Importar bibliotecas y configurar la figura

En el primer paso, importaremos las bibliotecas necesarias y configuraremos la figura y los ejes para el gráfico.

```python
import matplotlib.pyplot as plt
import numpy as np

# configurar la figura y los ejes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
```
