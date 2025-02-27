# Aplicar el agrupamiento K-Means

Ahora, aplicaremos el algoritmo de agrupamiento K-Means a nuestros datos. Inicializaremos el algoritmo con 3 clusters y lo ajustaremos a nuestros datos.

```python
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
```
