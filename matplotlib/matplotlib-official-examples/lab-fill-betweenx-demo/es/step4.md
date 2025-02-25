# Utilizando matrices con valores enmascarados

En este paso, aprenderemos cómo utilizar matrices con valores enmascarados para rellenar el área entre dos curvas horizontales.

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)
x2 = np.ma.masked_greater(x2, 1.0)

fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(x1, y, color='black')
ax.plot(x2, y, color='black')

ax.fill_betweenx(y, x1, x2, where=x2 >= x1, facecolor='verde', alpha=0.5)
ax.fill_betweenx(y, x1, x2, where=x2 <= x1, facecolor='rojo', alpha=0.5)

plt.show()
```
