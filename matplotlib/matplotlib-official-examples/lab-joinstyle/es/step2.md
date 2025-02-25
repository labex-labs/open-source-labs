# Creando un gráfico

Para crear un gráfico, primero debemos definir los datos que queremos trazar. En este ejemplo, usaremos la biblioteca `numpy` para generar algunos datos de muestra.

```python
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)
```

A continuación, creamos una nueva figura y eje usando `plt.subplots()`. Estableceremos los límites x e y del gráfico y luego trazaremos los datos usando `plot()`.

```python
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([-1.2, 1.2])
ax.plot(x, y)
```
