# Création d'une norme continue

Nous allons créer une norme continue pour mapper les points de données aux couleurs. Nous utiliserons la fonction `Normalize` de `matplotlib.pyplot` pour normaliser les valeurs de `dydx` entre son minimum et son maximum. Nous utiliserons ensuite la fonction `LineCollection` pour créer un ensemble de segments de ligne et les colorer individuellement en fonction de leur dérivée. Nous utiliserons la fonction `set_array` pour définir les valeurs utilisées pour la cartographie des couleurs.

```python
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
