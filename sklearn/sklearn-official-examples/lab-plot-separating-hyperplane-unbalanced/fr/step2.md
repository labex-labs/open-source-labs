# Création des données

Nous allons créer deux grappes de points aléatoires à l'aide de la fonction `make_blobs`. Nous allons créer une grappe avec 1000 points et une autre avec 100 points. Les centres des grappes seront respectivement `[0.0, 0.0]` et `[2.0, 2.0]`. Le paramètre `clusters_std` contrôle l'écart-type des grappes.

```python
n_samples_1 = 1000
n_samples_2 = 100
centers = [[0.0, 0.0], [2.0, 2.0]]
clusters_std = [1.5, 0.5]
X, y = make_blobs(
    n_samples=[n_samples_1, n_samples_2],
    centers=centers,
    cluster_std=clusters_std,
    random_state=0,
    shuffle=False,
)
```
