# `pcolormesh` Básico

Normalmente, especificamos um `pcolormesh` definindo a borda dos quadriláteros e o valor do quadrilátero. Observe que aqui _x_ e _y_ têm cada um um elemento extra do que Z na dimensão respectiva.

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
