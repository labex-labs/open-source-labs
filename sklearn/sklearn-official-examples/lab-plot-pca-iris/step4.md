# Perform PCA

Now that we have visualized the dataset, let's perform PCA on it. We will use scikit-learn's `PCA()` function for this. We will set the number of components to 3, as we want to reduce the dataset from 4 dimensions (4 features) to 3 dimensions.

```python
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
```
