# Image et barre de couleur avec positionnement au moment du tracé - Une manière difficile

Dans cette étape, nous allons créer une image et sa barre de couleur avec positionnement au moment du tracé de manière difficile. Nous utiliserons `SubplotDivider` de `mpl_toolkits.axes_grid1` pour créer un diviseur pour les axes et la barre de couleur.

```python
def demo_locatable_axes_hard(fig):
    from mpl_toolkits.axes_grid1 import Size, SubplotDivider

    divider = SubplotDivider(fig, 2, 2, 2, aspect=True)

    # axes pour l'image
    ax = fig.add_subplot(axes_locator=divider.new_locator(nx=0, ny=0))
    # axes pour la barre de couleur
    ax_cb = fig.add_subplot(axes_locator=divider.new_locator(nx=2, ny=0))

    divider.set_horizontal([
        Size.AxesX(ax),  # axes principaux
        Size.Fixed(0.05),  # marge, 0,1 pouce
        Size.Fixed(0.2),  # barre de couleur, 0,3 pouce
    ])
    divider.set_vertical([Size.AxesY(ax)])

    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.set_tick_params(labelright=False)
```
