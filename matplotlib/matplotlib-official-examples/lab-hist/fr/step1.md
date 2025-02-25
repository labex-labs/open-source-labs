# Générer des données et tracer un histogramme simple

Pour tracer un histogramme en 1D, nous avons seulement besoin d'un seul vecteur de nombres. Pour un histogramme en 2D, nous aurons besoin d'un second vecteur. Nous allons les générer ci-dessous et montrer l'histogramme pour chaque vecteur.

```python
import matplotlib.pyplot as plt
import numpy as np

# Crée un générateur de nombres aléatoires avec une graine fixe pour la reproductibilité
rng = np.random.default_rng(19680801)

N_points = 100000
n_bins = 20

# Génère deux distributions normales
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# Nous pouvons définir le nombre de barres avec l'argument clé *bins*.
axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)

plt.show()
```
