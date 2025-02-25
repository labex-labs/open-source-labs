# Begrenzungen des Plots festlegen

Legen Sie die Begrenzungen des Plots fest, indem Sie die `set`-Methode verwenden und die Grenzen der X-, Y- und Z-Koordinaten übergeben.

```python
# Set limits of the plot from coord limits
xmin, xmax = X.min(), X.max()
ymin, ymax = Y.min(), Y.max()
zmin, zmax = Z.min(), Z.max()
ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], zlim=[zmin, zmax])
```
