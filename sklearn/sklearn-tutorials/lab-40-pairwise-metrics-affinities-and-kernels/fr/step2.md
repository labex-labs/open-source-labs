# Noyaux

Les noyaux sont des mesures de similarité entre deux objets. Ils peuvent être utilisés dans diverses algorithmes d'apprentissage automatique pour capturer les relations non linéaires entre les caractéristiques.

Scikit-learn fournit différentes fonctions de noyau, telles que le noyau linéaire, le noyau polynomial, le noyau sigmoïde, le noyau RBF, le noyau Laplacien et le noyau chi-carré.

Calculons les noyaux entre paires de deux ensembles d'échantillons à l'aide de la fonction `pairwise_kernels` :

```python
from sklearn.metrics.pairwise import pairwise_kernels

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise kernels between X and Y using linear kernel
kernels = pairwise_kernels(X, Y, metric='linear')
print(kernels)
```

Sortie :

```
array([[ 2.,  7.],
       [ 3., 11.],
       [ 5., 18.]])
```
