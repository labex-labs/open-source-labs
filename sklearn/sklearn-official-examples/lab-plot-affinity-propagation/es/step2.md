# Generar datos de muestra

Generaremos un conjunto de datos de muestra utilizando la función `make_blobs` del módulo `sklearn.datasets`. La función `make_blobs` genera un conjunto de datos de puntos en un espacio de n dimensiones, donde cada punto pertenece a uno de los k clusters. Generaremos un conjunto de datos con 300 puntos en un espacio bidimensional, con 3 clusters y una desviación estándar de 0,5.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.5, random_state=0
)
```
