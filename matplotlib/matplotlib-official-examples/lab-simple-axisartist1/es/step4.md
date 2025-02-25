# Crear subtrama 2

En la segunda subtrama, usaremos `axisartist.axislines.AxesZero` para crear automáticamente los ejes xzero e yzero. Haremos que las otras espinas sean invisibles y haremos visible el eje xzero.

```python
ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Axis Zero")
ax1.axis["bottom", "top", "right"].set_visible(False)
```
