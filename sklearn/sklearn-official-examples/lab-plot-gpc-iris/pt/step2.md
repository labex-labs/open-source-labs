# Definindo a função kernel

Em seguida, definiremos a função kernel. Neste exemplo, usaremos o kernel Função de Base Radial (RBF). Definiremos duas versões do kernel RBF: uma versão isotrópica e uma versão anisotrópica.

```python
kernel = 1.0 * RBF([1.0])
gpc_rbf_isotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)

kernel = 1.0 * RBF([1.0, 1.0])
gpc_rbf_anisotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)
```
