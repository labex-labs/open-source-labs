# Anwenden des Spectral Co-Clustering-Algorithmus

Wir wenden den Spectral Co-Clustering-Algorithmus auf den gemischten Datensatz mit 5 Clustern an.

```python
model = SpectralCoclustering(n_clusters=5, random_state=0)
model.fit(data)
```
