# Importar bibliotecas y configurar el gráfico

El primer paso es importar las bibliotecas necesarias y configurar el gráfico. En este ejemplo, usaremos el módulo `pyplot` de Matplotlib y su herramienta `3d` para crear el gráfico 3D.

```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')
```
