# Definiendo la función del kernel

A continuación, definiremos la función del kernel. En este ejemplo, usaremos el kernel de Función Básica Radial (RBF, por sus siglas en inglés). Definiremos dos versiones del kernel RBF: una versión isotrópica y una versión anisotrópica.

```python
kernel = 1.0 * RBF([1.0])
gpc_rbf_isotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)

kernel = 1.0 * RBF([1.0, 1.0])
gpc_rbf_anisotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)
```
