# Trazado de líneas

En este paso, trazaremos un conjunto de líneas utilizando la biblioteca Matplotlib. Primero, creamos algunos datos aleatorios utilizando NumPy. A continuación, establecemos el ciclo de colores utilizando la función `cycler` para especificar la paleta de colores. Finalmente, trazamos los datos utilizando la función `plot` y llamamos a `legend()` para generar la leyenda.

```python
import matplotlib.pyplot as plt
import numpy as np

# Establece el estado aleatorio para la reproducibilidad
np.random.seed(19680801)

# Crea datos aleatorios
N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T

# Establece el ciclo de colores
cmap = plt.cm.coolwarm
plt.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# Traza los datos y genera la leyenda
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend()
```
