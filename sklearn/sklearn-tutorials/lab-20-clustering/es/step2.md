# Generar datos de muestra

A continuación, generemos algunos datos de muestra con los que trabajar. Utilizaremos la función `make_blobs` del módulo `sklearn.datasets` para crear un conjunto de datos sintético con clusters.

```python
# Generate sample data
X, y = make_blobs(n_samples=100, centers=4, random_state=0, cluster_std=1.0)
```
