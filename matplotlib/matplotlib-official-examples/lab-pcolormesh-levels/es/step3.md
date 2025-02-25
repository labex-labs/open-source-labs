# Coordenadas centradas

A menudo, un usuario desea pasar _X_ e _Y_ con los mismos tamaños que _Z_ a `.axes.Axes.pcolormesh`. Esto también está permitido si se pasa `shading='auto'` (valor predeterminado establecido por :rc:`pcolor.shading`). Antes de Matplotlib 3.3, `shading='flat'` eliminaba la última columna y la última fila de _Z_, pero ahora da un error. Si esto es realmente lo que desea, entonces simplemente elimine manualmente la última fila y la última columna de Z:

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(10)  # len = 10
y = np.arange(6)  # len = 6
X, Y = np.meshgrid(x, y)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
axs[0].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), shading='auto')
axs[0].set_title("shading='auto' = 'nearest'")
axs[1].pcolormesh(X, Y, Z[:-1, :-1], vmin=np.min(Z), vmax=np.max(Z),
                  shading='flat')
axs[1].set_title("shading='flat'")
```
