# Image et barre de couleur avec positionnement au moment du tracé - Une manière facile

Dans cette étape, nous allons créer une image et sa barre de couleur avec positionnement au moment du tracé d'une manière facile. Nous utiliserons `make_axes_locatable` de `mpl_toolkits.axes_grid1` pour créer un diviseur pour les axes et la barre de couleur.

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
