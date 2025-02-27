# Спектральное кластерирование

Мы будем использовать функцию `spectral_clustering` из `sklearn.cluster` для выполнения спектрального кластерирования. Параметр `n_clusters` установлен в 4, чтобы разделить четыре круга.

```python
from sklearn.cluster import spectral_clustering

labels = spectral_clustering(graph, n_clusters=4, eigen_solver="arpack")
```
