# Principal Component Analysis (PCA)

#### Exact PCA and probabilistic interpretation

Principal Component Analysis (PCA) is used to decompose a multivariate dataset into a set of successive orthogonal components that explain a maximum amount of variance. PCA can be implemented using the `PCA` class from scikit-learn. The `fit` method is used to learn the components, and the `transform` method can be used to project new data onto these components.

```python
from sklearn.decomposition import PCA

# Create a PCA object with n_components as the number of desired components
pca = PCA(n_components=2)

# Fit the PCA model to the data
pca.fit(data)

# Transform the data by projecting it onto the learned components
transformed_data = pca.transform(data)
```
