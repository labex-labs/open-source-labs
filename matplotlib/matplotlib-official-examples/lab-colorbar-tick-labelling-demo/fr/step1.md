# Importez les bibliothèques nécessaires et fixez l'état aléatoire

Tout d'abord, nous devons importer les bibliothèques nécessaires et fixer l'état aléatoire pour la reproductibilité. Nous utiliserons `numpy` pour générer des données aléatoires, `matplotlib.pyplot` pour créer des visualisations et `cm` de `matplotlib` pour définir les cartes de couleur.

```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

from matplotlib import cm

# Fixing random state for reproducibility
np.random.seed(19680801)
```
