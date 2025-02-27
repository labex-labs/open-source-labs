# Ajouter de forts outliers à l'ensemble de données

Nous allons ajouter quatre forts outliers à l'ensemble de données. Nous allons générer des valeurs aléatoires pour ces outliers en utilisant la distribution normale. Nous ajouterons ensuite ces outliers à l'ensemble de données.

```python
X_outliers = rng.normal(0, 0.5, size=(4, 1))
y_outliers = rng.normal(0, 2.0, size=4)
X_outliers[:2, :] += X.max() + X.mean() / 4.0
X_outliers[2:, :] += X.min() - X.mean() / 4.0
y_outliers[:2] += y.min() - y.mean() / 4.0
y_outliers[2:] += y.max() + y.mean() / 4.0
X = np.vstack((X, X_outliers))
y = np.concatenate((y, y_outliers))
```
