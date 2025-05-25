# `pcolormesh` Não Retilíneo

Observe que também podemos especificar matrizes para _X_ e _Y_ e ter quadriláteros não retilíneos.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7
X, Y = np.meshgrid(x, y)
X = X + 0.2 * Y  # tilt the coordinates.
Y = Y + 0.3 * X

fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z)
```
