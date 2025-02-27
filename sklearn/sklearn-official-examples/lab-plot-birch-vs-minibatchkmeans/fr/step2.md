# Générer des blobs

L'étape suivante consiste à générer des blobs pour comparer MiniBatchKMeans et BIRCH. Nous utiliserons toutes les couleurs que matplotlib fournit par défaut.

```python
# Générer des centres pour les blobs de manière à former une grille 10 X 10.
xx = np.linspace(-22, 22, 10)
yy = np.linspace(-22, 22, 10)
xx, yy = np.meshgrid(xx, yy)
n_centers = np.hstack((np.ravel(xx)[:, np.newaxis], np.ravel(yy)[:, np.newaxis]))

# Générer des blobs pour comparer MiniBatchKMeans et BIRCH.
X, y = make_blobs(n_samples=25000, centers=n_centers, random_state=0)

# Utiliser toutes les couleurs que matplotlib fournit par défaut.
colors_ = cycle(colors.cnames.keys())
```
