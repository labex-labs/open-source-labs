# Bild und Farbskala mit Zeichnungszeit-Positionierung - Ein schwieriger Weg

In diesem Schritt werden wir auf eine schwierige Weise ein Bild und seine Farbskala mit Zeichnungszeit-Positionierung erstellen. Wir werden `SubplotDivider` aus `mpl_toolkits.axes_grid1` verwenden, um einen Aufteiler für die Achsen und die Farbskala zu erstellen.

```python
def demo_locatable_axes_hard(fig):
    from mpl_toolkits.axes_grid1 import Size, SubplotDivider

    divider = SubplotDivider(fig, 2, 2, 2, aspect=True)

    # Achsen für das Bild
    ax = fig.add_subplot(axes_locator=divider.new_locator(nx=0, ny=0))
    # Achsen für die Farbskala
    ax_cb = fig.add_subplot(axes_locator=divider.new_locator(nx=2, ny=0))

    divider.set_horizontal([
        Size.AxesX(ax),  # Hauptachsen
        Size.Fixed(0.05),  # Innenabstand, 0,1 Zoll
        Size.Fixed(0.2),  # Farbskala, 0,3 Zoll
    ])
    divider.set_vertical([Size.AxesY(ax)])

    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.set_tick_params(labelright=False)
```
