# Définition de la fonction `confidence_ellipse`

Ensuite, nous définissons la fonction `confidence_ellipse` qui prendra en entrée les coordonnées x et y de l'ensemble de données, l'objet d'axes (axes object) dans lequel tracer l'ellipse et le nombre d'écarts-types. Elle renvoie un objet patch de Matplotlib représentant l'ellipse.

```python
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Crée un graphique de l'ellipse de confiance de covariance de *x* et *y*.

    Paramètres
    ----------
    x, y : semblable à un tableau, forme (n, )
        Données d'entrée.

    ax : matplotlib.axes.Axes
        L'objet d'axes dans lequel tracer l'ellipse.

    n_std : flottant
        Le nombre d'écarts-types pour déterminer les rayons de l'ellipse.

    **kwargs
        Transmis à `~matplotlib.patches.Ellipse`

    Retours
    -------
    matplotlib.patches.Ellipse
    """
    if x.size!= y.size:
        raise ValueError("x et y doivent avoir la même taille")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Utilisation d'un cas particulier pour obtenir les valeurs propres de cet
    # ensemble de données bidimensionnel.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calcul de l'écart-type de x à partir
    # de la racine carrée de la variance et multiplication
    # par le nombre donné d'écarts-types.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calcul de l'écart-type de y...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
       .rotate_deg(45) \
       .scale(scale_x, scale_y) \
       .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)
```
