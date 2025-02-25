# Das Histogramm erstellen

Jetzt, nachdem wir unsere Daten haben, können wir das 3D-Histogramm erstellen. Wir werden die `histogram2d()`-Funktion von NumPy verwenden, um ein 2D-Histogramm unserer Daten zu erstellen, und dann die `bar3d()`-Funktion von Matplotlib verwenden, um ein 3D-Säulendiagramm des Histogramms zu erstellen.

```python
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
```
