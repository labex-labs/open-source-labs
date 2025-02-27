# Entraîner le modèle

Nous allons utiliser un modèle GPC pour classifier les données. Tout d'abord, nous devons spécifier la fonction noyau.

```python
kernel = C(0.1, (1e-5, np.inf)) * DotProduct(sigma_0=0.1) ** 2
```

Ensuite, nous pouvons créer un modèle GPC et l'entraîner à l'aide des données.

```python
gp = GaussianProcessClassifier(kernel=kernel)
gp.fit(X, y)
```
