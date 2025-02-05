# 从 K-Means++ 计算种子

我们将使用 scikit-learn 库的 `kmeans_plusplus` 函数从 K-Means++ 计算种子。此函数返回用于 K-Means 聚类的初始聚类中心。我们将使用 K-Means++ 计算 4 个聚类。

```python
# 从 K-Means++ 计算种子
centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)
```
