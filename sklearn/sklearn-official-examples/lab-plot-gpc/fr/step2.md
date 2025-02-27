# Générer des données

Nous allons générer des données à l'aide de NumPy. Nous allons générer 100 points de données avec une distribution uniforme entre 0 et 5. Nous allons définir le seuil à 2,5 et générer les étiquettes à l'aide d'une expression booléenne. Nous utiliserons les 50 premiers points de données comme données d'entraînement et les autres comme données de test.

```python
train_size = 50
rng = np.random.RandomState(0)
X = rng.uniform(0, 5, 100)[:, np.newaxis]
y = np.array(X[:, 0] > 2.5, dtype=int)
```
