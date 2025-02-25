# Nicht-rectilineare pcolormesh

Beachten Sie, dass wir auch Matrizen für _X_ und _Y_ angeben können und nicht-rectilineare Vierecke haben.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # Länge = 11
y = np.arange(4.5, 11, 1)  # Länge = 7
X, Y = np.meshgrid(x, y)
X = X + 0.2 * Y  # Neigen Sie die Koordinaten.
Y = Y + 0.3 * X

fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z)
```
