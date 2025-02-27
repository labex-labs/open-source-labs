# Создаем модель

Далее мы создадим модель агломеративной кластеризации с использованием функции `AgglomerativeClustering()` из модуля `sklearn.cluster`.

```python
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
```
