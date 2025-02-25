# pcolormesh de base

Nous spécifions généralement un pcolormesh en définissant le bord des quadrilatères et la valeur du quadrilatère. Notez que ici, _x_ et _y_ ont chacun un élément supplémentaire par rapport à Z dans la dimension respective.

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
