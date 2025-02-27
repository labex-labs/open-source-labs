# Effectuez un regroupement avec MeanShift

Maintenant, nous allons effectuer un regroupement à l'aide de l'algorithme Mean-Shift avec la classe `MeanShift` du module `sklearn.cluster`. Nous utiliserons la fonction `estimate_bandwidth` pour détecter automatiquement le paramètre de largeur de bande, qui représente la taille de la région d'influence pour chaque point.

```python
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
```
