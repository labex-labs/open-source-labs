# Générer des données d'échantillonnage

Nous allons générer un ensemble de données composé d'une fonction cible sinusoïdale et de bruit fort ajouté à chaque cinquième point de données.

```python
import numpy as np

# Générer des données d'échantillonnage
rng = np.random.RandomState(42)
X = 5 * rng.rand(10000, 1)
y = np.sin(X).ravel()

# Ajouter du bruit aux cibles
y[::5] += 3 * (0.5 - rng.rand(X.shape[0] // 5))

X_plot = np.linspace(0, 5, 100000)[:, None]
```
