# Apply spectral clustering

We will apply spectral clustering using the default eigen_solver='arpack'. Any implemented solver can be used: eigen_solver='arpack', 'lobpcg', or 'amg'. Choosing eigen_solver='amg' requires an extra package called 'pyamg'. The quality of segmentation and the speed of calculations is mostly determined by the choice of the solver and the value of the tolerance 'eigen_tol'.

```python
# Apply spectral clustering using the default eigen_solver='arpack'.
# Any implemented solver can be used: eigen_solver='arpack', 'lobpcg', or 'amg'.
# Choosing eigen_solver='amg' requires an extra package called 'pyamg'.
# The quality of segmentation and the speed of calculations is mostly determined
# by the choice of the solver and the value of the tolerance 'eigen_tol'.
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
