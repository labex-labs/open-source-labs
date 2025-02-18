# Creación de un gráfico de barras con un valor alfa explícito

En este paso, crearemos un gráfico de barras utilizando el método `bar` en Matplotlib. Estableceremos el valor alfa utilizando el argumento de palabra clave `alpha`. Todas las barras del gráfico tendrán el mismo valor alfa.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility.
np.random.seed(19680801)

fig, ax = plt.subplots()

x_values = [n for n in range(20)]
y_values = np.random.randn(20)

facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors

ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)
ax.set_title("Explicit 'alpha' keyword value\nshared by all bars and edges")

plt.show()
```
