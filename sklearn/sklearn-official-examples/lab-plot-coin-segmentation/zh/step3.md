# 应用谱聚类

我们将使用默认的特征值求解器 `eigen_solver='arpack'` 来应用谱聚类。可以使用任何已实现的求解器：`eigen_solver='arpack'`、`'lobpcg'` 或 `'amg'`。选择 `eigen_solver='amg'` 需要一个名为 `'pyamg'` 的额外软件包。分割的质量和计算速度主要取决于求解器的选择以及容差 `eigen_tol` 的值。

```python
# 使用默认的特征值求解器eigen_solver='arpack'应用谱聚类。
# 可以使用任何已实现的求解器：eigen_solver='arpack'、'lobpcg' 或 'amg'。
# 选择eigen_solver='amg'需要一个名为'pyamg'的额外软件包。
# 分割的质量和计算速度主要取决于求解器的选择以及容差'eigen_tol'的值。
n_regions = 26
n_regions_plus = 3
for assign_labels in ("kmeans", "discretize", "cluster_qr"):
    t0 = time.time()
    labels = spectral_clustering(
        graph,
        n_clusters=(n_regions + n_regions_plus),
        eigen_tol=1e-7,
        assign_labels=assign_labels,
        random_state=42,
    )
    t1 = time.time()
    labels = labels.reshape(rescaled_coins.shape)
```
