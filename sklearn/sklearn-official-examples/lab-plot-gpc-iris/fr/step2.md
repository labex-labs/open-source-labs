# Définition de la fonction noyau

Ensuite, nous allons définir la fonction noyau. Dans cet exemple, nous utiliserons le noyau de fonction de base radiale (RBF en anglais). Nous allons définir deux versions du noyau RBF : une version isotrope et une version anisotrope.

```python
kernel = 1.0 * RBF([1.0])
gpc_rbf_isotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)

kernel = 1.0 * RBF([1.0, 1.0])
gpc_rbf_anisotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)
```
