# Dos imágenes una al lado de la otra con relleno fijo

En este paso, crearemos dos imágenes una al lado de la otra con un relleno fijo. Utilizaremos `make_axes_locatable` de `mpl_toolkits.axes_grid1` para crear un divisor para los ejes y la barra de color.

```python
def demo_images_side_by_side(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)

    Z, extent = get_demo_image()
    ax2 = divider.append_axes("right", size="100%", pad=0.05)
    fig1 = ax.get_figure()
    fig1.add_axes(ax2)

    ax.imshow(Z, extent=extent)
    ax2.imshow(Z, extent=extent)
    ax2.yaxis.set_tick_params(labelleft=False)
```
