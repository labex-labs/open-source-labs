# Graficando un relleno simple entre curvas horizontales

En este paso, aprenderemos cómo utilizar la función `fill_betweenx` para crear un gráfico simple. Rellenaremos el área entre dos curvas.

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)

fig, ax = plt.subplots(figsize=(6, 6))

ax.fill_betweenx(y, x1, x2, color='green', alpha=0.5)
ax.plot(x1, y, color='blue')
ax.plot(x2, y, color='red')

plt.show()
```
