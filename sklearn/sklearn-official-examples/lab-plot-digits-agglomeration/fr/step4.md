# Effectuer l'agglomération de fonctionnalités

Dans cette étape, nous allons effectuer l'agglomération de fonctionnalités à l'aide de la classe `FeatureAgglomeration` de scikit-learn. Nous allons définir le nombre de clusters sur 32.

```python
agglo = cluster.FeatureAgglomeration(connectivity=connectivity, n_clusters=32)
agglo.fit(X)
X_reduced = agglo.transform(X)
```
