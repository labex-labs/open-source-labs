# Crear la gráfica

El siguiente paso es crear la gráfica. Esto se puede hacer utilizando la función ContourSet.

```python
fig, ax = plt.subplots()

# Contornos rellenos usando filled=True.
cs = ContourSet(ax, [0, 1, 2], [filled01, filled12], filled=True, cmap=cm.bone)
cbar = fig.colorbar(cs)

# Líneas de contorno (no rellenas).
lines = ContourSet(
    ax, [0, 1, 2], [lines0, lines1, lines2], cmap=cm.cool, linewidths=3)
cbar.add_lines(lines)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 4.5),
       title='User-specified contours')
```
