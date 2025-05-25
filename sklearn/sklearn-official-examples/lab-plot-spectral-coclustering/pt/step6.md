# Aplicar o algoritmo Spectral Co-Clustering

Aplicamos o algoritmo Spectral Co-Clustering ao conjunto de dados embaralhado com 5 clusters.

```python
model = SpectralCoclustering(n_clusters=5, random_state=0)
model.fit(data)
```
