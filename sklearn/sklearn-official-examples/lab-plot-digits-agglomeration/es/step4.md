# Realizar la aglomeración de características

En este paso, realizaremos la aglomeración de características utilizando la clase `FeatureAgglomeration` de scikit-learn. Estableceremos el número de clusters en 32.

```python
agglo = cluster.FeatureAgglomeration(connectivity=connectivity, n_clusters=32)
agglo.fit(X)
X_reduced = agglo.transform(X)
```
