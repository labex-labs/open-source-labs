# Выполнить агломерацию признаков

В этом шаге мы выполним агломерацию признаков с использованием класса `FeatureAgglomeration` из scikit - learn. Мы установим количество кластеров равным 32.

```python
agglo = cluster.FeatureAgglomeration(connectivity=connectivity, n_clusters=32)
agglo.fit(X)
X_reduced = agglo.transform(X)
```
