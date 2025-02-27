# Вычисляем кластеризацию с использованием MeanShift

Теперь мы вычислим кластеризацию с использованием алгоритма MeanShift с классом `MeanShift` из модуля `sklearn.cluster`. Мы будем использовать функцию `estimate_bandwidth`, чтобы автоматически определить параметр ширины полосы, который представляет размер области влияния для каждой точки.

```python
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
```
