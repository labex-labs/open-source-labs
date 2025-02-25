# Bild und Farbskala mit Zeichnungszeit-Positionierung - Ein einfacher Weg

In diesem Schritt werden wir auf einfache Weise ein Bild und seine Farbskala mit Zeichnungszeit-Positionierung erstellen. Wir werden `make_axes_locatable` aus `mpl_toolkits.axes_grid1` verwenden, um einen Aufteiler für die Achsen und die Farbskala zu erstellen.

```python
def demo_locatable_axes_easy(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)

    ax_cb = divider.append_axes("right", size="5%", pad=0.05)
    fig = ax.get_figure()
    fig.add_axes(ax_cb)

    Z, extent = get_demo_image()
    im = ax.imshow(Z, extent=extent)

    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.tick_right()
    ax_cb.yaxis.set_tick_params(labelright=False)
```
