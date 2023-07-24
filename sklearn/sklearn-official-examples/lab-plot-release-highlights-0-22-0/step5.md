# Precomputed sparse nearest neighbors graph

Most estimators based on nearest neighbors graphs now accept precomputed sparse graphs as input, to reuse the same graph for multiple estimator fits.

```python
from tempfile import TemporaryDirectory
from sklearn.neighbors import KNeighborsTransformer
from sklearn.manifold import Isomap
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_classification

X, y = make_classification(random_state=0)

with TemporaryDirectory(prefix="sklearn_cache_") as tmpdir:
    estimator = make_pipeline(
        KNeighborsTransformer(n_neighbors=10, mode="distance"),
        Isomap(n_neighbors=10, metric="precomputed"),
        memory=tmpdir,
    )
    estimator.fit(X)

    estimator.set_params(isomap__n_neighbors=5)
    estimator.fit(X)
```
