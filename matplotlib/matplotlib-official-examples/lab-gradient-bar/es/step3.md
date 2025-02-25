# Definir la función de imagen de degradado

Necesitamos definir una función que creará una imagen de degradado basada en una mapa de colores. Esta función tomará un objeto de ejes, la dirección del degradado y el rango del mapa de colores que se utilizará. Luego, la función generará la imagen de degradado y la devolverá.

```python
def gradient_image(ax, direction=0.3, cmap_range=(0, 1), **kwargs):
    """
    Dibuja una imagen de degradado basada en un mapa de colores.

    Parámetros
    ----------
    ax : Ejes
        Los ejes en los que se dibujará.
    direction : float
        La dirección del degradado. Este es un número en
        el rango 0 (=vertical) a 1 (=horizontal).
    cmap_range : float, float
        La fracción (cmin, cmax) del mapa de colores que debe ser
        utilizada para el degradado, donde el mapa de colores completo es (0, 1).
    **kwargs
        Otros parámetros se transmiten a `.Axes.imshow()`.
        En particular, *cmap*, *extent* y *transform* pueden ser útiles.
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
