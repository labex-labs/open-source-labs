# Générer des données d'échantillonnage

Nous allons générer un ensemble de données d'échantillonnage à l'aide de la fonction `make_blobs` du module `sklearn.datasets`. La fonction `make_blobs` génère un ensemble de données de points dans un espace à n dimensions, chaque point appartenant à l'un des k groupes. Nous allons générer un ensemble de données avec 300 points dans un espace à 2 dimensions, avec 3 groupes et une déviation standard de 0,5.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.5, random_state=0
)
```
