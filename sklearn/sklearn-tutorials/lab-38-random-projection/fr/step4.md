# Projection aléatoire sparse

Ensuite, essayons un autre type de projection aléatoire appelé projection aléatoire sparse.

```python
transformer = random_projection.SparseRandomProjection()
X_new = transformer.fit_transform(X)
```

Ici, nous créons une instance de la classe `SparseRandomProjection` et l'appliquons à nos données `X` en utilisant la méthode `fit_transform`. Le résultat est stocké dans la variable `X_new`.
