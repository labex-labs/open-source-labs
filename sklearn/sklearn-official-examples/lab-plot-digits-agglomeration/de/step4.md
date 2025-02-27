# Feature Agglomeration durchführen

In diesem Schritt werden wir Feature Agglomeration mit der Klasse `FeatureAgglomeration` aus scikit-learn durchführen. Wir werden die Anzahl der Cluster auf 32 setzen.

```python
agglo = cluster.FeatureAgglomeration(connectivity=connectivity, n_clusters=32)
agglo.fit(X)
X_reduced = agglo.transform(X)
```
