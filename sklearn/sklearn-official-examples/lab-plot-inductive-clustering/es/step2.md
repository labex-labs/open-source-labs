# Entrenar el algoritmo de agrupamiento

En este paso, entrenaremos un algoritmo de agrupamiento con los datos de entrenamiento generados y obtendremos las etiquetas de los clusters. Usaremos `AgglomerativeClustering` de scikit-learn para entrenar el algoritmo con 3 clusters.

```python
clusterer = AgglomerativeClustering(n_clusters=3)
cluster_labels = clusterer.fit_predict(X)
```
