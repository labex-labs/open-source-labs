# Perform Feature Agglomeration

In this step, we will perform feature agglomeration using the `FeatureAgglomeration` class from scikit-learn. We will set the number of clusters to 32.

```python
agglo = cluster.FeatureAgglomeration(connectivity=connectivity, n_clusters=32)
agglo.fit(X)
X_reduced = agglo.transform(X)
```
