# Orden personalizado de los elementos

También podemos establecer el `zorder` de los elementos en un orden personalizado. Por ejemplo, podemos establecer el `zorder` de una leyenda para que quede entre dos líneas.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 7.5, 100)
plt.rcParams['lines.linewidth'] = 5
plt.figure()
plt.plot(x, np.sin(x), label='zorder=2', zorder=2)  # bottom
plt.plot(x, np.sin(x+0.5), label='zorder=3',  zorder=3)
plt.axhline(0, label='zorder=2.5', color='lightgrey', zorder=2.5)
plt.title('Custom order of elements')
l = plt.legend(loc='upper right')
l.set_zorder(2.5)  # legend between blue and orange line
plt.show()
```
