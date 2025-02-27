# Optimiser la largeur de bande

Nous utilisons la validation croisée par recherche sur grille pour optimiser le paramètre de largeur de bande de la KDE. Le paramètre de largeur de bande contrôle la lissité de l'estimation de densité.

```python
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
import numpy as np

# utiliser la validation croisée par recherche sur grille pour optimiser la largeur de bande
params = {"bandwidth": np.logspace(-1, 1, 20)}
grid = GridSearchCV(KernelDensity(), params)
grid.fit(data)

print("meilleure largeur de bande : {0}".format(grid.best_estimator_.bandwidth))

# utiliser le meilleur estimateur pour calculer l'estimation de densité par noyau
kde = grid.best_estimator_
```
