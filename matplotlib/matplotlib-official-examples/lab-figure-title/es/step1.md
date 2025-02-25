# Crea un gráfico de oscilación amortiguada y no amortiguada

Primero, crearemos una figura con dos subgráficos, uno para una oscilación amortiguada y otro para una oscilación no amortiguada. Utilizaremos la función `np.linspace()` para crear una matriz de valores de tiempo y luego graficaremos los valores correspondientes de amplitud para cada tipo de oscilación utilizando las funciones `np.cos()` y `np.exp()`.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey=True)
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('amortiguada')
ax1.set_xlabel('tiempo (s)')
ax1.set_ylabel('amplitud')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('tiempo (s)')
ax2.set_title('no amortiguada')

fig.suptitle('Diferentes tipos de oscilaciones', fontsize=16)

plt.show()
```
