# Establece los límites de la gráfica

Establece los límites de la gráfica utilizando el método `set` y pasando los límites de las coordenadas X, Y y Z.

```python
# Establece los límites de la gráfica a partir de los límites de las coordenadas
xmin, xmax = X.min(), X.max()
ymin, ymax = Y.min(), Y.max()
zmin, zmax = Z.min(), Z.max()
ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], zlim=[zmin, zmax])
```
