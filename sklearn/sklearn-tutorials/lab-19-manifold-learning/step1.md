# Isomap

The Isomap algorithm is one of the earliest approaches to manifold learning. It seeks a lower-dimensional embedding that maintains geodesic distances between all points.

```python
from sklearn.manifold import Isomap

# Create an instance of the Isomap algorithm
isomap = Isomap(n_components=2)

# Fit the algorithm to the data and transform the data to the lower-dimensional space
X_transformed = isomap.fit_transform(X)
```
