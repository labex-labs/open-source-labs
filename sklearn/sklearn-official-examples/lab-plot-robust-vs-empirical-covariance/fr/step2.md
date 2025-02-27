# Générer des données

Dans cette étape, nous générons un ensemble de données aléatoires avec `n_samples` échantillons et `n_features` caractéristiques. Nous ajoutons également quelques valeurs aberrantes à l'ensemble de données.

```python
n_samples = 80
n_features = 5

# Générer un ensemble de données aléatoire
rng = np.random.RandomState(42)
X = rng.randn(n_samples, n_features)

# Ajouter des valeurs aberrantes à l'ensemble de données
n_outliers = 20
outliers_index = rng.permutation(n_samples)[:n_outliers]
outliers_offset = 10.0 * (
    np.random.randint(2, size=(n_outliers, n_features)) - 0.5
)
X[outliers_index] += outliers_offset
```
