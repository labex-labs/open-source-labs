# Construisez l'ensemble de données

Dans cette étape, nous allons créer un ensemble de données de classification non linéairement séparable composé de deux grappes de quantiles gaussiennes à l'aide de la fonction `make_gaussian_quantiles` du module `sklearn.datasets`. Nous allons également concaténer les deux grappes et leur attribuer des étiquettes.

```python
X1, y1 = make_gaussian_quantiles(
    cov=2.0, n_samples=200, n_features=2, n_classes=2, random_state=1
)
X2, y2 = make_gaussian_quantiles(
    mean=(3, 3), cov=1.5, n_samples=300, n_features=2, n_classes=2, random_state=1
)
X = np.concatenate((X1, X2))
y = np.concatenate((y1, -y2 + 1))
```
