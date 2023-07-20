# Centered coordinates

Often a user wants to pass _X_ and _Y_ with the same sizes as _Z_ to `.axes.Axes.pcolormesh`. This is also allowed if `shading='auto'` is passed (default set by :rc:`pcolor.shading`). Pre Matplotlib 3.3, `shading='flat'` would drop the last column and row of _Z_, but now gives an error. If this is really what you want, then simply drop the last row and column of Z manually:

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
