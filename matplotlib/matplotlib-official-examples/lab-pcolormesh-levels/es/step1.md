# pcolormesh básico

Por lo general, especificamos un pcolormesh definiendo el borde de los cuadriláteros y el valor del cuadrilátero. Tenga en cuenta que aquí _x_ e _y_ tienen un elemento adicional en cada dimensión en comparación con Z.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)
```
