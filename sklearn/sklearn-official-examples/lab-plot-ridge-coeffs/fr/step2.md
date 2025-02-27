# Générer des données aléatoires

Nous allons générer des données aléatoires avec la fonction `make_regression` de scikit-learn. Nous allons définir `n_samples` sur 10, `n_features` sur 10 et `random_state` sur 1. Cette fonction retournera nos caractéristiques d'entrée X, notre variable cible y et les valeurs réelles des coefficients w.

```python
X, y, w = make_regression(
    n_samples=10, n_features=10, coef=True, random_state=1, bias=3.5
)
```
