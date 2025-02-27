# Préparer les données

Dans cette étape, nous allons préparer les ensembles de données de classification synthétiques pour la discrétisation des fonctionnalités. Nous utiliserons la bibliothèque scikit-learn pour générer trois ensembles de données différents : des lunules, des cercles concentriques et des données linéairement séparables.

```python
h = 0.02  # pas dans la grille
n_samples = 100
datasets = [
    make_moons(n_samples=n_samples, noise=0.2, random_state=0),
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1),
    make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        random_state=2,
        n_clusters_per_class=1,
    ),
]
```
