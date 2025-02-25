# Grundlegende pcolormesh

Wir definieren normalerweise eine pcolormesh, indem wir den Rand von Vierecken und den Wert des Vierecks definieren. Beachten Sie, dass hier _x_ und _y_ jeweils ein zusätzliches Element im jeweiligen Dimension haben als Z.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # Länge = 11
y = np.arange(4.5, 11, 1)  # Länge = 7

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)
```
