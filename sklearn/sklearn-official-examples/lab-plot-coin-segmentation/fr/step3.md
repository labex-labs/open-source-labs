# Appliquer le regroupement spectral

Nous allons appliquer le regroupement spectral en utilisant le solveur d'eigenvaleur par défaut `eigen_solver='arpack'`. N'importe quel solveur implémenté peut être utilisé : `eigen_solver='arpack'`, `'lobpcg'` ou `'amg'`. Choisir `eigen_solver='amg'` nécessite un package supplémentaire appelé `'pyamg'`. La qualité de la segmentation et la vitesse des calculs sont principalement déterminées par le choix du solveur et la valeur de la tolérance `eigen_tol`.

```python
# Appliquer le regroupement spectral en utilisant le solveur d'eigenvaleur par défaut `eigen_solver='arpack'`.
# N'importe quel solveur implémenté peut être utilisé : `eigen_solver='arpack'`, `'lobpcg'` ou `'amg'`.
# Choisir `eigen_solver='amg'` nécessite un package supplémentaire appelé `'pyamg'`.
# La qualité de la segmentation et la vitesse des calculs sont principalement déterminées
# par le choix du solveur et la valeur de la tolérance `eigen_tol`.
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
