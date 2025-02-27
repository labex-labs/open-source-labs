# Кластеризация с использованием K-means

Первая техника, которую мы исследуем, - это кластеризация с использованием алгоритма K-means. K-means - популярный алгоритм кластеризации, который имеет целью разделить наблюдения на хорошо отделенные группы, называемые кластерами. Возьмем в качестве примера датасет Iris, чтобы продемонстрировать кластеризацию с использованием K-means.

```python
from sklearn import cluster, datasets

# Load the Iris dataset
X_iris, y_iris = datasets.load_iris(return_X_y=True)

# Perform K-means clustering
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

# Print the cluster labels
print(k_means.labels_)
```
