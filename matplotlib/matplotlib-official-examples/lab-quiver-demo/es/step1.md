# Las flechas se escalan con el ancho de la gráfica, no con la vista

La función `quiver()` se puede utilizar para crear un gráfico de flechas. Por defecto, las flechas en el gráfico se escalarán con los datos, en lugar de con el gráfico mismo. Esto puede dificultar la visualización de las flechas que se encuentran cerca del borde del gráfico.

```python
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi,.2), np.arange(0, 2 * np.pi,.2))
U = np.cos(X)
V = np.sin(Y)

fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='width')
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
plt.show()
```
