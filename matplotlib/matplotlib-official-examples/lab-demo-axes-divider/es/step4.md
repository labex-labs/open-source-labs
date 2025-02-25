# Imagen y barra de color con posicionamiento en tiempo de dibujo: una forma difícil

En este paso, crearemos una imagen y su barra de color con posicionamiento en tiempo de dibujo de una manera difícil. Utilizaremos `SubplotDivider` de `mpl_toolkits.axes_grid1` para crear un divisor para los ejes y la barra de color.

```python
def demo_locatable_axes_hard(fig):
    from mpl_toolkits.axes_grid1 import Size, SubplotDivider

    divider = SubplotDivider(fig, 2, 2, 2, aspect=True)

    # ejes para la imagen
    ax = fig.add_subplot(axes_locator=divider.new_locator(nx=0, ny=0))
    # ejes para la barra de color
    ax_cb = fig.add_subplot(axes_locator=divider.new_locator(nx=2, ny=0))

    divider.set_horizontal([
        Size.AxesX(ax),  # ejes principales
        Size.Fixed(0.05),  # relleno, 0.1 pulgada
        Size.Fixed(0.2),  # barra de color, 0.3 pulgada
    ])
    divider.set_vertical([Size.AxesY(ax)])

    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.set_tick_params(labelright=False)
```
