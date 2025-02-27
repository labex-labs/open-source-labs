# Aplicar el agrupamiento espectral

Aplicaremos el agrupamiento espectral utilizando el eigen_solver='arpack' por defecto. Se puede utilizar cualquier resolvente implementado: eigen_solver='arpack', 'lobpcg' o 'amg'. Elegir eigen_solver='amg' requiere un paquete adicional llamado 'pyamg'. La calidad de la segmentación y la velocidad de cálculo se determinan en gran medida por la elección del resolvente y el valor de la tolerancia 'eigen_tol'.

```python
# Aplicar el agrupamiento espectral utilizando el eigen_solver='arpack' por defecto.
# Se puede utilizar cualquier resolvente implementado: eigen_solver='arpack', 'lobpcg', o 'amg'.
# Elegir eigen_solver='amg' requiere un paquete adicional llamado 'pyamg'.
# La calidad de la segmentación y la velocidad de cálculo se determinan en gran medida
# por la elección del resolvente y el valor de la tolerancia 'eigen_tol'.
n_regiones = 26
n_regiones_más = 3
for assign_labels in ("kmeans", "discretize", "cluster_qr"):
    t0 = time.time()
    labels = spectral_clustering(
        grafica,
        n_clusters=(n_regiones + n_regiones_más),
        eigen_tol=1e-7,
        assign_labels=assign_labels,
        random_state=42,
    )
    t1 = time.time()
    labels = labels.reshape(monedas_redimensionadas.shape)
```
