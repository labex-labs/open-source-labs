# Configurar el divisor de ejes

Configuraremos el divisor de ejes utilizando la clase `Divider` y las clases `AxesX` y `AxesY` del módulo `mpl_toolkits.axes_grid1.axes_size`. Luego, usaremos el método `new_locator` para establecer la posición de cada eje.

```python
horiz = [Size.AxesX(ax[0]), Size.Fixed(.5), Size.AxesX(ax[1])]
vert = [Size.AxesY(ax[0]), Size.Fixed(.5), Size.AxesY(ax[2])]
divider = Divider(fig, rect, horiz, vert, aspect=False)

ax[0].set_axes_locator(divider.new_locator(nx=0, ny=0))
ax[1].set_axes_locator(divider.new_locator(nx=2, ny=0))
ax[2].set_axes_locator(divider.new_locator(nx=0, ny=2))
ax[3].set_axes_locator(divider.new_locator(nx=2, ny=2))
```
