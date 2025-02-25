# Creando múltiples subgráficos

En este paso, aprenderemos cómo crear múltiples subgráficos y utilizar la función `fill_betweenx` para rellenar el área entre dos curvas horizontales en cada subgráfico.

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)

fig, [ax1, ax2, ax3] = plt.subplots(1, 3, sharey=True, figsize=(12, 4))

ax1.fill_betweenx(y, 0, x1, color='green', alpha=0.5)
ax1.plot(x1, y, color='blue')
ax1.set_title('Relleno entre (x1, 0)')

ax2.fill_betweenx(y, x1, 1, color='red', alpha=0.5)
ax2.plot(x1, y, color='blue')
ax2.set_title('Relleno entre (x1, 1)')

ax3.fill_betweenx(y, x1, x2, color='naranja', alpha=0.5)
ax3.plot(x1, y, color='blue')
ax3.plot(x2, y, color='rojo')
ax3.set_title('Relleno entre (x1, x2)')

plt.show()
```
