# Visualiser le résultat après la réduction de dimension avec Truncated SVD

Dans cette étape, nous allons visualiser le résultat après la réduction de dimension avec Truncated SVD.

```python
svd = TruncatedSVD(n_components=2)
X_reduced = svd.fit_transform(X_transformed)
```
