# Générer des données d'échantillonnage

Ensuite, générons quelques données d'échantillonnage avec lesquelles travailler. Nous utiliserons la fonction `make_blobs` du module `sklearn.datasets` pour créer un ensemble de données synthétiques avec des clusters.

```python
# Generate sample data
X, y = make_blobs(n_samples=100, centers=4, random_state=0, cluster_std=1.0)
```
