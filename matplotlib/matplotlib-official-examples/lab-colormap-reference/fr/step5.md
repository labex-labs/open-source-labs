# Création de cartes de couleurs personnalisées

Matplotlib offre également la possibilité de créer des cartes de couleurs personnalisées. Cela peut être utile lorsque les cartes de couleurs intégrées ne fournissent pas la représentation souhaitée des données.

```python
import matplotlib.colors as mcolors

# Définir une liste de couleurs et leurs valeurs correspondantes
couleurs = [(0,'red'), (0.5, 'green'), (1, 'blue')]

# Créer un objet LinearSegmentedColormap à partir de la liste de couleurs
cmap = mcolors.LinearSegmentedColormap.from_list('my_cmap', couleurs)
```
