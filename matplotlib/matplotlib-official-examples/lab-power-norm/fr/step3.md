# Créer des données

Dans cette étape, vous devez créer des données à l'aide de `multivariate_normal()`. Cette fonction génère un échantillon aléatoire à partir d'une distribution normale multivariée.

```python
data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[3, 1], [1, 3]], size=1000)
])
```
