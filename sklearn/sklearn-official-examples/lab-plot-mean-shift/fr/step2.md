# Générez des données d'échantillonnage

Ensuite, nous allons générer des données d'échantillonnage à l'aide de la fonction `make_blobs` du module `sklearn.datasets`. Nous allons créer un ensemble de données avec 10 000 échantillons et trois grappes avec des centres à `[[1, 1], [-1, -1], [1, -1]]` et une déviation standard de 0,6.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
```
