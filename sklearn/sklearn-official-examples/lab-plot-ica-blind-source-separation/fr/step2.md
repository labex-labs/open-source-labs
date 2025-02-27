# Ajuster les modèles ICA et PCA

Nous utiliserons FastICA pour estimer les sources indépendantes. Nous calculerons ensuite la PCA pour la comparaison.

```python
from sklearn.decomposition import FastICA, PCA

# Calculer l'ICA
ica = FastICA(n_components=3, whiten="arbitrary-variance")
S_ = ica.fit_transform(X)  # Reconstruire les signaux
A_ = ica.mixing_  # Obtenir la matrice de mélange estimée

# Nous pouvons `prouver` que le modèle ICA s'applique en inversant le démélange.
assert np.allclose(X, np.dot(S_, A_.T) + ica.mean_)

# Pour la comparaison, calculer la PCA
pca = PCA(n_components=3)
H = pca.fit_transform(X)  # Reconstruire les signaux basés sur les composantes orthogonales
```
