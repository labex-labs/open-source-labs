# Ejecutar el algoritmo de clustering OPTICS

Ahora ejecutaremos el algoritmo de clustering OPTICS en los datos generados. En este ejemplo, establecemos `min_samples = 50`, `xi = 0.05` y `min_cluster_size = 0.05`.

```python
clust = OPTICS(min_samples=50, xi=0.05, min_cluster_size=0.05)
clust.fit(X)
```
