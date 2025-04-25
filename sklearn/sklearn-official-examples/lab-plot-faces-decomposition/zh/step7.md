# 聚类中心 - 小批量 K 均值算法（MiniBatchKMeans）

K 均值聚类是一种通过最小化每个点与其所属聚类的质心之间的平方距离之和，将数据集划分为多个聚类的方法。我们应用小批量 K 均值算法（MiniBatchKMeans），它是 K 均值算法（KMeans）的一个更快版本，更适合处理大型数据集。

```python
# 聚类中心 - 小批量 K 均值算法（MiniBatchKMeans）
kmeans_estimator = cluster.MiniBatchKMeans(
    n_clusters=n_components,
    tol=1e-3,
    batch_size=20,
    max_iter=50,
    random_state=rng,
    n_init="auto",
)
kmeans_estimator.fit(faces_centered)
plot_gallery(
    "聚类中心 - 小批量 K 均值算法（MiniBatchKMeans）",
    kmeans_estimator.cluster_centers_[:n_components],
)
```
