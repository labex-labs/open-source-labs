# Définissez la fonction d'image à gradient

Nous devons définir une fonction qui créera une image à gradient basée sur une carte de couleurs. Cette fonction prendra un objet d'axes, la direction du gradient et la plage de la carte de couleurs à utiliser. La fonction générera ensuite l'image à gradient et la renverra.

```python
def gradient_image(ax, direction=0.3, cmap_range=(0, 1), **kwargs):
    """
    Dessine une image à gradient basée sur une carte de couleurs.

    Paramètres
    ----------
    ax : Axes
        Les axes sur lesquels dessiner.
    direction : float
        La direction du gradient. Il s'agit d'un nombre dans
        la plage 0 (=vertical) à 1 (=horizontal).
    cmap_range : float, float
        La fraction (cmin, cmax) de la carte de couleurs qui doit être
        utilisée pour le gradient, où la carte de couleurs complète est (0, 1).
    **kwargs
        Autres paramètres sont transmis à `.Axes.imshow()`.
        En particulier, *cmap*, *extent* et *transform* peuvent être utiles.
    """
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    X = np.array([[v @ [1, 0], v @ [1, 1]],
                  [v @ [0, 0], v @ [0, 1]]])
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    im = ax.imshow(X, interpolation='bicubic', clim=(0, 1),
                   aspect='auto', **kwargs)
    return im
```
