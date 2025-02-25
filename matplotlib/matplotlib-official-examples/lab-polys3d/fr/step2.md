# Définissez la fonction du polygone sous le graphique

Ensuite, nous définissons une fonction `polygon_under_graph(x, y)` qui construit la liste de sommets qui définit le polygone remplissant l'espace sous le graphique en ligne (x, y). Cette fonction suppose que x est dans l'ordre croissant.

```python
def polygon_under_graph(x, y):
    """
    Construit la liste de sommets qui définit le polygone remplissant l'espace sous
    le graphique en ligne (x, y). Cela suppose que x est dans l'ordre croissant.
    """
    return [(x[0], 0.), *zip(x, y), (x[-1], 0.)]
```
