# Générer des données d'échantillonnage

Nous allons utiliser la fonction `make_blobs` de la bibliothèque scikit-learn pour générer des données d'échantillonnage. Cette fonction génère des grappes gaussiennes isotrope pour le regroupement. Nous allons générer 4000 échantillons avec 4 centres.

```python
# Générer des données d'échantillonnage
n_samples = 4000
n_components = 4

X, y_true = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)
X = X[:, ::-1]
```
