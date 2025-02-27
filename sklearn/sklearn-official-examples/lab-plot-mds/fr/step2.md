# Générer des données

Ensuite, nous allons générer un ensemble de données bruité à l'aide de numpy. Nous allons générer 20 échantillons avec 2 caractéristiques chacun.

```python
EPSILON = np.finfo(np.float32).eps
n_samples = 20
seed = np.random.RandomState(seed=3)
X_true = seed.randint(0, 20, 2 * n_samples).astype(float)
X_true = X_true.reshape((n_samples, 2))
# Center the data
X_true -= X_true.mean()
```
