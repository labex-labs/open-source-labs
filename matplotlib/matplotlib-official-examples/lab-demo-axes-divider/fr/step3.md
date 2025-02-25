# Image simple et barre de couleur

Dans cette étape, nous allons créer une image simple et sa barre de couleur. Nous utiliserons la fonction `imshow()` de `pyplot` pour créer l'image et la fonction `colorbar()` pour créer la barre de couleur.

```python
def demo_simple_image(ax):
    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)
```
