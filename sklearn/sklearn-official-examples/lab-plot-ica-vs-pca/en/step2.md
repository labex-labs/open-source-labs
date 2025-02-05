# Use PCA Algorithm

In this step, we use PCA algorithm to find orthogonal directions in the raw feature space that correspond to directions accounting for maximum variance.

```python
pca = PCA()
S_pca_ = pca.fit(X).transform(X)
```
