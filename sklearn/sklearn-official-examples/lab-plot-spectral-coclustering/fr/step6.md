# Appliquer l'algorithme de co-clustering spectral

Nous appliquons l'algorithme de co-clustering spectral à l'ensemble de données mélangé avec 5 clusters.

```python
model = SpectralCoclustering(n_clusters=5, random_state=0)
model.fit(data)
```
