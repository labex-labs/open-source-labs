# クラスタ中心 - MiniBatchKMeans

K-means クラスタリングは、各点とその割り当てられたクラスタの重心との間の二乗距離の和を最小化することにより、データセットをクラスタに分割する方法です。私たちは、大規模なデータセットにより適した、KMeans の高速バージョンである MiniBatchKMeans を適用します。

```python
# クラスタ中心 - MiniBatchKMeans
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
    "Cluster centers - MiniBatchKMeans",
    kmeans_estimator.cluster_centers_[:n_components],
)
```
