# Обучение алгоритма кластеризации

В этом шаге мы обучим алгоритм кластеризации на сгенерированных обучающих данных и получим метки кластеров. Мы будем использовать `AgglomerativeClustering` из scikit-learn для обучения алгоритма с 3 кластерами.

```python
clusterer = AgglomerativeClustering(n_clusters=3)
cluster_labels = clusterer.fit_predict(X)
```
