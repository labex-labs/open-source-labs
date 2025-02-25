# Configurez le diviseur d'axes

Nous allons configurer le diviseur d'axes à l'aide de la classe `Divider` et des classes `AxesX` et `AxesY` du module `mpl_toolkits.axes_grid1.axes_size`. Ensuite, nous utiliserons la méthode `new_locator` pour définir la position de chaque axe.

```python
horiz = [Size.AxesX(ax[0]), Size.Fixed(.5), Size.AxesX(ax[1])]
vert = [Size.AxesY(ax[0]), Size.Fixed(.5), Size.AxesY(ax[2])]
divider = Divider(fig, rect, horiz, vert, aspect=False)

ax[0].set_axes_locator(divider.new_locator(nx=0, ny=0))
ax[1].set_axes_locator(divider.new_locator(nx=2, ny=0))
ax[2].set_axes_locator(divider.new_locator(nx=0, ny=2))
ax[3].set_axes_locator(divider.new_locator(nx=2, ny=2))
```
