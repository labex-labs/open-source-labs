# Anwenden der spectralen Clustering-Methode

Wir werden die spectrale Clustering-Methode mit dem Standard-Wert eigen_solver='arpack' anwenden. Es kann jeder implementierte Solver verwendet werden: eigen_solver='arpack', 'lobpcg' oder 'amg'. Die Verwendung von eigen_solver='amg' erfordert ein zusätzliches Paket namens 'pyamg'. Die Qualität der Segmentierung und die Rechengeschwindigkeit werden hauptsächlich durch die Wahl des Solvers und den Wert der Toleranz 'eigen_tol' bestimmt.

```python
# Anwenden Sie die spectrale Clustering-Methode mit dem Standard-Wert eigen_solver='arpack'.
# Es kann jeder implementierte Solver verwendet werden: eigen_solver='arpack', 'lobpcg' oder 'amg'.
# Die Verwendung von eigen_solver='amg' erfordert ein zusätzliches Paket namens 'pyamg'.
# Die Qualität der Segmentierung und die Rechengeschwindigkeit werden hauptsächlich bestimmt
# durch die Wahl des Solvers und den Wert der Toleranz 'eigen_tol'.
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
