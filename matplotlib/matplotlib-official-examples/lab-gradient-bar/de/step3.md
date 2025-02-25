# Definieren der Gradientenbildfunktion

Wir müssen eine Funktion definieren, die ein Gradientenbild basierend auf einer Farbskala erstellt. Diese Funktion wird ein Achsenobjekt, die Richtung des Gradienten und den Bereich der zu verwendenden Farbskala entgegennehmen. Die Funktion wird dann das Gradientenbild generieren und zurückgeben.

```python
def gradient_image(ax, direction=0.3, cmap_range=(0, 1), **kwargs):
    """
    Zeichnet ein Gradientenbild basierend auf einer Farbskala.

    Parameter
    ----------
    ax : Axes
        Die Achsen, auf denen gezeichnet werden soll.
    direction : float
        Die Richtung des Gradienten. Dies ist eine Zahl im
        Bereich 0 (=vertikal) bis 1 (=horizontal).
    cmap_range : float, float
        Der Anteil (cmin, cmax) der Farbskala, der für den Gradienten
        verwendet werden soll, wobei die komplette Farbskala (0, 1) ist.
    **kwargs
        Andere Parameter werden an `.Axes.imshow()` weitergeleitet.
        Insbesondere *cmap*, *extent* und *transform* können nützlich sein.
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
