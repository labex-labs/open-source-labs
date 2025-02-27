# Charger l'ensemble de données

Nous utiliserons la fonction `make_gaussian_quantiles` de `sklearn.datasets` pour générer un ensemble de données. Cette fonction génère des Gaussiennes isotropes et ajoute une séparation entre les classes pour rendre le problème plus difficile.

```python
X, y = make_gaussian_quantiles(
    n_samples=13000, n_features=10, n_classes=3, random_state=1
)
```
