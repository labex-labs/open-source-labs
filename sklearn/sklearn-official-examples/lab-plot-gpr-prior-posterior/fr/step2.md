# Création des données d'entraînement

Ensuite, nous créons un ensemble de données d'entraînement que nous utiliserons dans les différentes sections.

```python
rng = np.random.RandomState(4)
X_train = rng.uniform(0, 5, 10).reshape(-1, 1)
y_train = np.sin((X_train[:, 0] - 2.5) ** 2)
n_samples = 5
```
