# Zwei Bilder nebeneinander mit fester Innenabstand

In diesem Schritt werden wir zwei Bilder nebeneinander mit fester Innenabstand erstellen. Wir werden `make_axes_locatable` aus `mpl_toolkits.axes_grid1` verwenden, um einen Aufteiler für die Achsen und die Farbskala zu erstellen.

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
