# Créez un ensemble de données aléatoire

Nous allons créer un ensemble de données aléatoire à l'aide de NumPy et y ajouter du bruit.

```python
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))
```
