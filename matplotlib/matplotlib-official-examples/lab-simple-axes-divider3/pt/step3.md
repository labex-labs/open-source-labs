# Configurar o divisor de eixos

Configuraremos o divisor de eixos usando a classe `Divider` e as classes `AxesX` e `AxesY` do módulo `mpl_toolkits.axes_grid1.axes_size`. Em seguida, usaremos o método `new_locator` para definir a posição de cada eixo.

```python
horiz = [Size.AxesX(ax[0]), Size.Fixed(.5), Size.AxesX(ax[1])]
vert = [Size.AxesY(ax[0]), Size.Fixed(.5), Size.AxesY(ax[2])]
divider = Divider(fig, rect, horiz, vert, aspect=False)

ax[0].set_axes_locator(divider.new_locator(nx=0, ny=0))
ax[1].set_axes_locator(divider.new_locator(nx=2, ny=0))
ax[2].set_axes_locator(divider.new_locator(nx=0, ny=2))
ax[3].set_axes_locator(divider.new_locator(nx=2, ny=2))
```
