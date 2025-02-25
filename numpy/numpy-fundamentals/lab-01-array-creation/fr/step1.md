# Conversion de séquences Python en tableaux NumPy

Pour créer des tableaux NumPy, vous pouvez convertir des séquences Python telles que des listes et des tuples. Voici comment faire :

```python
import numpy as np

# Créez un tableau 1D à partir d'une liste
a1D = np.array([1, 2, 3, 4])

# Créez un tableau 2D à partir d'une liste de listes
a2D = np.array([[1, 2], [3, 4]])

# Créez un tableau 3D à partir de listes imbriquées
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

Lors de la création de tableaux, vous pouvez également spécifier le type de données à l'aide du paramètre `dtype`. Soyez prudent lors des affectations de type de données pour éviter les débordements ou des résultats inattendus.
