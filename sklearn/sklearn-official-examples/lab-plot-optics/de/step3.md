# OPTICS-Clustering-Algorithmus ausführen

Wir werden nun den OPTICS-Clustering-Algorithmus auf den generierten Daten ausführen. In diesem Beispiel setzen wir `min_samples=50`, `xi=0.05` und `min_cluster_size=0.05`.

```python
clust = OPTICS(min_samples=50, xi=0.05, min_cluster_size=0.05)
clust.fit(X)
```
