# Importation des bibliothèques et chargement des données

Nous commencerons par importer les bibliothèques nécessaires et charger les jeux de données de démonstration que nous utiliserons pour nos exemples de regroupement hiérarchique.

```python
import time
import warnings

import numpy as np
import matplotlib.pyplot as plt

from sklearn import cluster, datasets
from sklearn.preprocessing import StandardScaler
from itertools import cycle, islice

np.random.seed(0)

# %%
# Génération des jeux de données. Nous choisissons une taille suffisamment grande pour voir la
# capacité d'échelle des algorithmes, mais pas trop grande pour éviter des temps d'exécution trop longs

n_samples = 1500
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.05)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)
no_structure = np.random.rand(n_samples, 2), None

# Données distribuées de manière anisotrope
random_state = 170
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)

# Blobs avec des variances variées
varied = datasets.make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)
```
