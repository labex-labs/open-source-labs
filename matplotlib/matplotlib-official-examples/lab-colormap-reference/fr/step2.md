# Création d'une carte de couleurs simple

Pour créer une carte de couleurs simple, nous pouvons utiliser la classe `ListedColormap` du module `matplotlib.colors`. Cette classe prend une liste de couleurs et en crée une carte de couleurs.

```python
import matplotlib.colors as mcolors

# Définir une liste de couleurs
couleurs = ['red', 'green', 'blue']

# Créer un objet ListedColormap à partir de la liste de couleurs
cmap = mcolors.ListedColormap(couleurs)
```
