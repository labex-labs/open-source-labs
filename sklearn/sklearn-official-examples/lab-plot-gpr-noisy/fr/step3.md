# Ajout de bruit

Dans cette étape, nous allons ajouter du bruit aux données générées pour créer un ensemble de données d'entraînement plus réaliste.

```python
rng = np.random.RandomState(0)
X_train = rng.uniform(0, 5, size=20).reshape(-1, 1)
y_train = target_generator(X_train, add_noise=True)
```
