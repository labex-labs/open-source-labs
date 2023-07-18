# Perform PCA

Next, we will perform PCA on our dataset. We first concatenate `x`, `y`, and `z` to form a 3D array `Y`. We then create an instance of the PCA class and fit it to our data. We can then access the principal components using the `components_` attribute of the PCA object.

```python
Y = np.c_[x, y, z]
pca = PCA(n_components=3)
pca.fit(Y)
components = pca.components_
```
