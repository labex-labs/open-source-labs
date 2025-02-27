# Применение алгоритма K-Means Clustering

Теперь мы применим алгоритм K-Means Clustering к нашим данным. Мы инициализируем алгоритм с 3 кластерами и подгоняем его под наши данные.

```python
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
```
