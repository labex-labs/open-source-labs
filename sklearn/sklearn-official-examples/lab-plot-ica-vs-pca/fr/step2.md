# Utiliser l'algorithme PCA

Dans cette étape, nous utilisons l'algorithme PCA pour trouver des directions orthogonales dans l'espace de caractéristiques brutes qui correspondent à des directions représentant la variance maximale.

```python
pca = PCA()
S_pca_ = pca.fit(X).transform(X)
```
