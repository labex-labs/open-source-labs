# Perform PCA

We will perform PCA on the Iris dataset by initializing an instance of the PCA class and fitting it to the data.

```python
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)
```
