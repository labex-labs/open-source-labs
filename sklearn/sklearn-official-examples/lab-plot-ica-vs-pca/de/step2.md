# PCA-Algorithmus verwenden

In diesem Schritt verwenden wir den PCA-Algorithmus, um orthogonale Richtungen im ursprünglichen Merkmalsraum zu finden, die den Richtungen entsprechen, die für die maximale Varianz verantwortlich sind.

```python
pca = PCA()
S_pca_ = pca.fit(X).transform(X)
```
