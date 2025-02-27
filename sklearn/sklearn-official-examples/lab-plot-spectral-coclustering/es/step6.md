# Aplicar el algoritmo de Co-Clustering Espectral

Aplicamos el algoritmo de Co-Clustering Espectral al conjunto de datos mezclado con 5 clusters.

```python
model = SpectralCoclustering(n_clusters=5, random_state=0)
model.fit(data)
```
