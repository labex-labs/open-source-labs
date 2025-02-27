# Transformée inverse

Les transformateurs de projection aléatoire ont une option pour calculer l'inverse de la matrice de projection. Explorons cette fonctionnalité en appliquant la transformée inverse à nos données projetées.

```python
transformer = random_projection.SparseRandomProjection(compute_inverse_components=True)
X_new = transformer.fit_transform(X)

# Compute the inverse transform
X_new_inversed = transformer.inverse_transform(X_new)
```

Dans cette étape, nous créons une instance de la classe `SparseRandomProjection` avec le paramètre `compute_inverse_components` défini sur `True`. Ensuite, nous ajustons le transformateur à nos données `X` et appliquons la transformation. Enfin, nous calculons la transformée inverse en appelant la méthode `inverse_transform` sur les données projetées `X_new`.
