# Definition der Funktion `confidence_ellipse`

Als Nächstes definieren wir die Funktion `confidence_ellipse`, die die x- und y-Koordinaten des Datensatzes, das Achsenobjekt, in das die Ellipse gezeichnet werden soll, und die Anzahl der Standardabweichungen als Parameter erhält. Sie gibt ein Matplotlib-Patch-Objekt zurück, das die Ellipse repräsentiert.

```python
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Erstellt ein Diagramm der Kovarianz-Konfidenzellipse von *x* und *y*.

    Parameter
    ----------
    x, y : array-ähnlich, Form (n, )
        Eingabedaten.

    ax : matplotlib.axes.Axes
        Das Achsenobjekt, in das die Ellipse gezeichnet werden soll.

    n_std : float
        Die Anzahl der Standardabweichungen, um die Radien der Ellipse zu bestimmen.

    **kwargs
        Weitergeleitet an `~matplotlib.patches.Ellipse`

    Rückgabewert
    -------
    matplotlib.patches.Ellipse
    """
    if x.size!= y.size:
        raise ValueError("x und y müssen die gleiche Größe haben")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Verwendung eines Spezialfalls, um die Eigenwerte dieses
    # zweidimensionalen Datensatzes zu erhalten.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Berechnung der Standardabweichung von x aus
    # der Quadratwurzel der Varianz und Multiplikation
    # mit der angegebenen Anzahl der Standardabweichungen.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # Berechnung der Standardabweichung von y...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
       .rotate_deg(45) \
       .scale(scale_x, scale_y) \
       .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)
```
