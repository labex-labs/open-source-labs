# Générer des données

Nous allons générer des données d'échantillonnage à l'aide de la fonction `make_blobs` de la bibliothèque `sklearn.datasets`. Cette fonction génère des grappes gaussiennes isotropes pour le regroupement en grappes.

```python
X, y = make_blobs(
    n_samples=500,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=1,
)  # Pour la reproductibilité
```
