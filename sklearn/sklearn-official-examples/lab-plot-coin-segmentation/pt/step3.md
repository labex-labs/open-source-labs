# Aplicar agrupamento espectral

Aplicaremos agrupamento espectral usando o solucionador padrão `eigen_solver='arpack'`. Qualquer solucionador implementado pode ser usado: `eigen_solver='arpack'`, `'lobpcg'` ou `'amg'`. A escolha de `eigen_solver='amg'` requer um pacote adicional chamado `'pyamg'`. A qualidade da segmentação e a velocidade dos cálculos dependem principalmente da escolha do solucionador e do valor da tolerância `'eigen_tol'`.

```python
# Aplicar agrupamento espectral usando o solucionador padrão eigen_solver='arpack'.
# Qualquer solucionador implementado pode ser usado: eigen_solver='arpack', 'lobpcg' ou 'amg'.
# A escolha de eigen_solver='amg' requer um pacote adicional chamado 'pyamg'.
# A qualidade da segmentação e a velocidade dos cálculos dependem principalmente da escolha do solucionador e do valor da tolerância 'eigen_tol'.
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
