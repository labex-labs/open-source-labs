# Вычисление DBSCAN

Мы будем использовать класс DBSCAN из модуля sklearn.cluster для вычисления кластеров. Мы установим параметр eps равным 0,3 и параметр min_samples равным 10. Мы можем получить метки, назначенные DBSCAN, с использованием атрибута labels. Шумовые образцы получают метку -1. Мы также вычислим количество кластеров и количество шумовых точек.

```python
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics

db = DBSCAN(eps=0.3, min_samples=10).fit(X)
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
```
