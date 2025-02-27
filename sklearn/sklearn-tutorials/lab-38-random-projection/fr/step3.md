# Projection aléatoire gaussienne

Maintenant, appliquons la projection aléatoire gaussienne pour réduire la dimensionalité de nos données.

```python
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
```

Dans cette étape, nous créons une instance de la classe `GaussianRandomProjection` et l'ajustons à nos données `X`. Ensuite, nous appliquons la transformation en appelant la méthode `fit_transform`. Le résultat est stocké dans la variable `X_new`.
