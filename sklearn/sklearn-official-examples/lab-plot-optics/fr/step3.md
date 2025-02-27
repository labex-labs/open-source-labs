# Exécuter l'algorithme de clustering OPTICS

Nous allons maintenant exécuter l'algorithme de clustering OPTICS sur les données générées. Dans cet exemple, nous définissons `min_samples = 50`, `xi = 0,05` et `min_cluster_size = 0,05`.

```python
clust = OPTICS(min_samples=50, xi=0.05, min_cluster_size=0.05)
clust.fit(X)
```
