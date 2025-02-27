# Generar datos de muestra

A continuación, generaremos datos de muestra utilizando la función `make_blobs` del módulo `sklearn.datasets`. Crearemos un conjunto de datos con 10.000 muestras y tres clusters con centros en `[[1, 1], [-1, -1], [1, -1]]` y una desviación estándar de 0,6.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
```
