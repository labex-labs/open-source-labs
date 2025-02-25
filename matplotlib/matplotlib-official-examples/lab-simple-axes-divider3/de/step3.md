# Einrichten des Achsenbereichs

Wir werden den Achsenbereich mit der `Divider`-Klasse und den `AxesX`- und `AxesY`-Klassen aus dem `mpl_toolkits.axes_grid1.axes_size`-Modul einrichten. Anschließend werden wir die `new_locator`-Methode verwenden, um die Position jeder Achse festzulegen.

```python
horiz = [Size.AxesX(ax[0]), Size.Fixed(.5), Size.AxesX(ax[1])]
vert = [Size.AxesY(ax[0]), Size.Fixed(.5), Size.AxesY(ax[2])]
divider = Divider(fig, rect, horiz, vert, aspect=False)

ax[0].set_axes_locator(divider.new_locator(nx=0, ny=0))
ax[1].set_axes_locator(divider.new_locator(nx=2, ny=0))
ax[2].set_axes_locator(divider.new_locator(nx=0, ny=2))
ax[3].set_axes_locator(divider.new_locator(nx=2, ny=2))
```
