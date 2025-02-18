# Définition de la fonction de Lorenz

Nous définissons la fonction de Lorenz, qui prend trois paramètres et renvoie un tableau de trois valeurs. Nous utilisons les valeurs par défaut `s = 10`, `r = 28` et `b = 2.667` pour les paramètres de Lorenz.

```python
def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Paramètres
    ----------
    xyz : semblable à un tableau, de forme (3,)
       Point d'intérêt dans l'espace tridimensionnel.
    s, r, b : flottants
       Paramètres définissant l'attracteur de Lorenz.

    Retourne
    -------
    xyz_dot : tableau, de forme (3,)
       Valeurs des dérivées partielles de l'attracteur de Lorenz en *xyz*.
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])
```
