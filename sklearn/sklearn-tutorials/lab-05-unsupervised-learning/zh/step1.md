# 使用 K 均值算法进行聚类

我们要探索的第一种技术是使用 K 均值算法进行聚类。K 均值是一种流行的聚类算法，旨在将观测值划分为称为簇的、分得很开的组。让我们以鸢尾花数据集为例来演示使用 K 均值算法进行聚类。

```python
from sklearn import cluster, datasets

# 加载鸢尾花数据集
X_iris, y_iris = datasets.load_iris(return_X_y=True)

# 执行 K 均值聚类
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

# 打印簇标签
print(k_means.labels_)
```
