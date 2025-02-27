# Création des données

Nous allons créer trois ensembles de données différents pour illustrer l'utilisation de t-SNE. Le premier ensemble de données sera deux cercles concentriques.

```python
n_samples = 150
n_components = 2

X, y = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=0
)

red = y == 0
green = y == 1
```
