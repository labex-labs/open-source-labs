# Locally Linear Embedding (LLE)

Locally Linear Embedding (LLE) is another manifold learning algorithm. It seeks a lower-dimensional projection of the data that preserves distances within local neighborhoods.

```python
from sklearn.manifold import LocallyLinearEmbedding

# Create an instance of the LLE algorithm
lle = LocallyLinearEmbedding(n_components=2)

# Fit the algorithm to the data and transform the data to the lower-dimensional space
X_transformed = lle.fit_transform(X)
```
