# Mélangez les données

Pour assurer l'aléatoire dans notre analyse, mélangeons l'ordre des échantillons dans notre ensemble de données.

```python
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]
```
