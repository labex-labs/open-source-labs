# Agrupamiento utilizando K-means

La primera técnica que exploraremos es el agrupamiento utilizando el algoritmo K-means. K-means es un algoritmo de agrupamiento popular que tiene como objetivo dividir las observaciones en grupos bien separados llamados clusters. Usemos el conjunto de datos Iris como ejemplo para demostrar el agrupamiento con K-means.

```python
from sklearn import cluster, datasets

# Cargar el conjunto de datos Iris
X_iris, y_iris = datasets.load_iris(return_X_y=True)

# Realizar el agrupamiento K-means
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

# Imprimir las etiquetas de los clusters
print(k_means.labels_)
```
