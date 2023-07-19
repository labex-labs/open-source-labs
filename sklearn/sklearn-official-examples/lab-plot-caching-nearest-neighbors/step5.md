# Cache Nearest Neighbors Graph

In this step, we will cache the nearest neighbors graph between multiple fits of KNeighborsClassifier using the caching property of pipelines.

```python
# Note that we give `memory` a directory to cache the graph computation
# that will be used several times when tuning the hyperparameters of the
# classifier.
with TemporaryDirectory(prefix="sklearn_graph_cache_") as tmpdir:
    full_model = Pipeline(
        steps=[("graph", graph_model), ("classifier", classifier_model)], memory=tmpdir
    )
```
