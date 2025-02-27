# Vérification

Pour vérifier la correction de la transformée inverse, nous pouvons comparer les données originales `X` avec le résultat de la transformée inverse.

```python
X_new_again = transformer.transform(X_new_inversed)
np.allclose(X_new, X_new_again)
```

Ici, nous appliquons la transformation aux données transformées inversement `X_new_inversed` et vérifions si elle est égale aux données projetées originales `X_new` en utilisant la fonction `np.allclose`.
