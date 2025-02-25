# Créer des axes insets

Ensuite, nous allons créer des axes insets dans chacun des sous-graphiques. Nous utiliserons la méthode `inset_axes()` pour créer les axes insets. Nous allons créer quatre insets avec différentes tailles et emplacements.

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Crée un inset de largeur 1,3 pouces et hauteur 0,9 pouces
# à l'emplacement supérieur droit par défaut
axins = inset_axes(ax, width=1.3, height=0.9)

# Crée un inset de largeur 30% et hauteur 40% de la boîte englobante
# des axes parentes
# dans le coin inférieur gauche (loc=3)
axins2 = inset_axes(ax, width="30%", height="40%", loc=3)

# Crée un inset avec des spécifications mixtes dans le second sous-graphique ;
# la largeur est de 30% de la boîte englobante des axes parentes et
# la hauteur est de 1 pouce dans le coin supérieur gauche (loc=2)
axins3 = inset_axes(ax2, width="30%", height=1., loc=2)

# Crée un inset dans le coin inférieur droit (loc=4) avec borderpad=1, c'est-à-dire
# un rembourrage de 10 points (car 10pt est la taille de police par défaut)
# par rapport aux axes parentes
axins4 = inset_axes(ax2, width="20%", height="20%", loc=4, borderpad=1)
```
